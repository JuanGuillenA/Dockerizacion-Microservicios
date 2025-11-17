from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import os, psycopg

app = FastAPI(title="users-service", version="1.0.0")

# ============================
# Configuración de la base de datos
# ============================
DB_NAME = os.getenv("POSTGRES_DB", "usersdb")
DB_USER = os.getenv("POSTGRES_USER", "usersuser")
DB_PASS = os.getenv("POSTGRES_PASSWORD", "supersecret")
DB_HOST = os.getenv("DB_HOST", "db")
DB_PORT = os.getenv("POSTGRES_PORT", "5432")

TEAM_MEMBERS = [
    ("Juan Alberto Guillén", "Backend · Coordinador", "0105730865", "juan.guillen@gmail.com"),
    ("Ariel Solano", "Developer · Docker", "0706664034", "Ariel.Solano@gmail.com"),
    ("Kevin Sinchi", "Frontend · Documentación", "0999999999", "Kevin.Sinchi@gmail.com"),
]


def db_conn():
    return psycopg.connect(
        dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST, port=DB_PORT
    )



@app.get("/", response_class=HTMLResponse)
def home():
    html = """
    <!doctype html>
    <html lang="es">
    <head>
      <meta charset="utf-8" />
      <title>Microservicio con Docker Compose de Juan Guillen</title>
      <meta name="viewport" content="width=device-width, initial-scale=1" />
      <style>
        :root{
          --bg:#0f172a;
          --card:#020617;
          --accent:#38bdf8;
          --text:#e5e7eb;
          --muted:#9ca3af;
        }
        *{box-sizing:border-box;margin:0;padding:0;}
        body{
          min-height:100vh;
          display:flex;
          align-items:center;
          justify-content:center;
          font-family:system-ui,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;
          background: radial-gradient(circle at top, #1e293b 0, #020617 55%, #000 100%);
          color:var(--text);
          padding:24px;
        }
        .container{
          max-width:960px;
          width:100%;
          background:rgba(15,23,42,0.9);
          border-radius:24px;
          padding:32px 28px 26px;
          box-shadow:0 25px 80px rgba(0,0,0,0.75);
          border:1px solid rgba(148,163,184,0.35);
          backdrop-filter: blur(18px);
        }
        .badge{
          display:inline-flex;
          align-items:center;
          gap:8px;
          padding:4px 10px;
          border-radius:999px;
          border:1px solid rgba(148,163,184,0.7);
          font-size:12px;
          letter-spacing:0.08em;
          text-transform:uppercase;
          color:var(--muted);
          margin-bottom:10px;
        }
        .badge-dot{
          width:8px;height:8px;border-radius:999px;
          background:radial-gradient(circle at 30% 30%, #bbf7d0 0, #22c55e 40%, #16a34a 100%);
          box-shadow:0 0 16px rgba(34,197,94,0.8);
        }
        h1{
          font-size:28px;
          line-height:1.2;
          margin-bottom:6px;
        }
        .subtitle{
          font-size:14px;
          color:var(--muted);
          margin-bottom:18px;
        }
        .highlight{
          color:var(--accent);
          font-weight:600;
        }
        .grid{
          display:grid;
          grid-template-columns:repeat(auto-fit,minmax(220px,1fr));
          gap:18px;
          margin-top:18px;
        }
        .card{
          background:linear-gradient(145deg,#020617,#020617);
          border-radius:18px;
          padding:16px 14px 14px;
          border:1px solid rgba(148,163,184,0.35);
        }
        .card-header{
          display:flex;
          justify-content:space-between;
          align-items:center;
          margin-bottom:8px;
        }
        .name{
          font-weight:600;
          font-size:16px;
        }
        .role{
          font-size:12px;
          color:var(--accent);
          text-transform:uppercase;
          letter-spacing:0.08em;
        }
        .pill{
          font-size:11px;
          padding:3px 8px;
          border-radius:999px;
          border:1px solid rgba(148,163,184,0.6);
          color:var(--muted);
        }
        .info{
          font-size:13px;
          color:var(--muted);
          margin-top:4px;
        }
        .footer{
          margin-top:22px;
          font-size:12px;
          color:var(--muted);
          display:flex;
          justify-content:space-between;
          flex-wrap:wrap;
          gap:8px;
          align-items:center;
        }
        .tag{
          padding:3px 10px;
          border-radius:999px;
          background:rgba(15,23,42,0.9);
          border:1px solid rgba(56,189,248,0.7);
          font-size:11px;
          color:var(--accent);
        }
        .actions{
          margin-top:18px;
          display:flex;
          flex-wrap:wrap;
          gap:10px;
          align-items:center;
        }
        .btn-primary{
          border:none;
          border-radius:999px;
          padding:8px 18px;
          font-size:13px;
          font-weight:500;
          background:linear-gradient(135deg,#0ea5e9,#22c55e);
          color:#0b1120;
          cursor:pointer;
        }
        .btn-secondary{
          border-radius:999px;
          padding:7px 14px;
          font-size:12px;
          text-decoration:none;
          border:1px solid rgba(148,163,184,0.7);
          color:var(--muted);
          background:transparent;
          cursor:pointer;
        }
        .msg{
          font-size:12px;
          color:var(--muted);
        }
      </style>
    </head>
    <body>
      <main class="container">
        <div class="badge">
          <span class="badge-dot"></span>
          Microservicio desplegado con Docker Compose
        </div>

        <h1>Plataforma de ejemplo con <span class="highlight">microservicios</span></h1>
        <p class="subtitle">
          Esta página la cree siendo utilizada por un contenedor Docker que forma parte de un
          <span class="highlight">microservicio backend</span> orquestado con
          <span class="highlight">Docker Compose</span>.
        </p>

        <div class="grid">
          <section class="card">
            <div class="card-header">
              <div>
                <div class="name">Juan Alberto Guillén</div>
                <div class="role">Backend · Coordinador</div>
              </div>
              <span class="pill">Integrante 1</span>
            </div>
            <p class="info">
              Cédula: 0105730865<br>
              Email: juan.guillen@gmail.com<br>
              Universidad de Cuenca – Ing. en Ciencias de la Computación.
            </p>
          </section>

          <section class="card">
            <div class="card-header">
              <div>
                <div class="name">Ariel Solano</div>
                <div class="role">Developer · Docker</div>
              </div>
              <span class="pill">Integrante 2</span>
            </div>
            <p class="info">
              Cédula: 0706664034<br>
              Email: Ariel.Solano@gmail.com<br>
              Responsable del despliegue con Docker y Docker Compose.
            </p>
          </section>

          <section class="card">
            <div class="card-header">
              <div>
                <div class="name">Kevin Sinchi</div>
                <div class="role">Frontend · Documentación</div>
              </div>
              <span class="pill">Integrante 3</span>
            </div>
            <p class="info">
              Cédula: 0999999999<br>
              Email: Kevin.Sinchi@gmail.com<br>
              Encargado de la presentación y diseño de interfaces.
            </p>
          </section>
        </div>

        <div class="actions">
          <button id="seedBtn" class="btn-primary">
            Registrar integrantes en la base de datos
          </button>
          <button id="clearBtn" class="btn-secondary">
            Borrar integrantes de la base de datos
          </button>
          <a href="/users" class="btn-secondary">Ver tabla de integrantes (/users)</a>
          <span id="seedResult" class="msg"></span>
        </div>

        <div class="footer">
          <span>Estado del servicio: <span class="highlight">ONLINE</span> </span>
          <span class="tag">FastAPI · PostgreSQL · Docker Compose</span>
        </div>
      </main>

      <script>
        const seedBtn = document.getElementById("seedBtn");
        const clearBtn = document.getElementById("clearBtn");
        const msg = document.getElementById("seedResult");

        seedBtn.addEventListener("click", async () => {
          msg.textContent = "Registrando integrantes...";
          try {
            const res = await fetch("/seed-team", { method: "POST" });
            const data = await res.json();
            msg.textContent = data.message;
          } catch (e) {
            msg.textContent = "Error al registrar integrantes.";
          }
        });

        clearBtn.addEventListener("click", async () => {
          msg.textContent = "Borrando integrantes...";
          try {
            const res = await fetch("/clear-team", { method: "POST" });
            const data = await res.json();
            msg.textContent = data.message;
          } catch (e) {
            msg.textContent = "Error al borrar integrantes.";
          }
        });
      </script>
    </body>
    </html>
    """
    return html


# ============================
# Endpoint para insertar el equipo en la BD
# ============================
@app.post("/seed-team")
def seed_team():
    with db_conn() as conn:
        with conn.cursor() as cur:
            # Creamos la tabla de integrantes si no existe
            cur.execute(
                """
                CREATE TABLE IF NOT EXISTS team_members (
                    id SERIAL PRIMARY KEY,
                    name   TEXT NOT NULL,
                    role   TEXT NOT NULL,
                    cedula TEXT NOT NULL,
                    email  TEXT NOT NULL UNIQUE
                );
                """
            )

            for name, role, cedula, email in TEAM_MEMBERS:
                cur.execute(
                    """
                    INSERT INTO team_members (name, role, cedula, email)
                    VALUES (%s, %s, %s, %s)
                    ON CONFLICT (email) DO UPDATE
                      SET name = EXCLUDED.name,
                          role = EXCLUDED.role,
                          cedula = EXCLUDED.cedula;
                    """,
                    (name, role, cedula, email),
                )
        conn.commit()

    return {"message": "Integrantes registrados/actualizados correctamente ✔"}



@app.post("/clear-team")
def clear_team():
    with db_conn() as conn:
        with conn.cursor() as cur:
            # Nos aseguramos de que la tabla exista y luego la vaciamos
            cur.execute(
                """
                CREATE TABLE IF NOT EXISTS team_members (
                    id SERIAL PRIMARY KEY,
                    name   TEXT NOT NULL,
                    role   TEXT NOT NULL,
                    cedula TEXT NOT NULL,
                    email  TEXT NOT NULL UNIQUE
                );
                """
            )
            cur.execute("TRUNCATE TABLE team_members;")
        conn.commit()

    return {"message": "Integrantes eliminados correctamente ✔"}



@app.get("/users", response_class=HTMLResponse)
def list_users():
    with db_conn() as conn:
        with conn.cursor() as cur:
            # Aseguramos la tabla
            cur.execute(
                """
                CREATE TABLE IF NOT EXISTS team_members (
                    id SERIAL PRIMARY KEY,
                    name   TEXT NOT NULL,
                    role   TEXT NOT NULL,
                    cedula TEXT NOT NULL,
                    email  TEXT NOT NULL UNIQUE
                );
                """
            )
            cur.execute(
                "SELECT name, role, cedula, email FROM team_members ORDER BY id;"
            )
            rows = cur.fetchall()

    rows_html = ""
    if rows:
        for idx, (name, role, cedula, email) in enumerate(rows, start=1):
            rows_html += f"""
            <tr>
              <td>{idx}</td>
              <td>{name}</td>
              <td>{role}</td>
              <td>{cedula}</td>
              <td>{email}</td>
            </tr>
            """
    else:
        rows_html = """
        <tr>
          <td colspan="5">No hay integrantes registrados aún.
          Usa el botón en la página principal para cargarlos.</td>
        </tr>
        """

    html_head = """
    <!doctype html>
    <html lang="es">
    <head>
      <meta charset="utf-8" />
      <title>Integrantes registrados</title>
      <meta name="viewport" content="width=device-width, initial-scale=1" />
      <style>
        body{
          font-family:system-ui,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;
          background:#020617;
          color:#e5e7eb;
          padding:24px;
        }
        h1{
          font-size:24px;
          margin-bottom:12px;
        }
        a{
          color:#38bdf8;
          text-decoration:none;
          font-size:13px;
        }
        table{
          width:100%;
          border-collapse:collapse;
          margin-top:12px;
          background:#020617;
          border-radius:16px;
          overflow:hidden;
          box-shadow:0 20px 60px rgba(0,0,0,0.7);
        }
        thead{
          background:#0f172a;
        }
        th,td{
          padding:10px 12px;
          font-size:13px;
        }
        th{
          text-align:left;
          color:#a5b4fc;
          border-bottom:1px solid rgba(148,163,184,0.4);
        }
        tr:nth-child(even){
          background:#020617;
        }
        tr:nth-child(odd){
          background:#020617;
        }
        tr + tr td{
          border-top:1px solid rgba(148,163,184,0.18);
        }
      </style>
    </head>
    <body>
      <h1>Integrantes registrados en la base de datos</h1>
      <p style="font-size:13px;">
        Esta tabla se alimenta desde PostgreSQL dentro del contenedor <strong>users-db</strong>.
        Los datos se insertan desde el microservicio <strong>users-api</strong> usando Docker Compose.
      </p>
      <p style="margin-top:6px;"><a href="/">← Volver a la página principal</a></p>

      <table>
        <thead>
          <tr>
            <th>#</th>
            <th>Nombre</th>
            <th>Rol</th>
            <th>Cédula</th>
            <th>Email</th>
          </tr>
        </thead>
        <tbody>
    """

    html_tail = """
        </tbody>
      </table>
    </body>
    </html>
    """

    return HTMLResponse(html_head + rows_html + html_tail)


# ============================
# /health (JSON para Docker) + /health-ui (bonito para humanos)
# ============================
@app.get("/health")
def health():
    try:
        with db_conn() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT 1;")
        return {"status": "ok"}
    except Exception as e:
        return {"status": "error", "detail": str(e)}


@app.get("/health-ui", response_class=HTMLResponse)
def health_ui():
    try:
        with db_conn() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT 1;")
        status_text = "ONLINE..."
        color = "#22c55e"
        detail = "Servicio y base de datos funcionando correctamente."
    except Exception as e:
        status_text = "ERROR"
        color = "#ef4444"
        detail = f"Problema al conectar a la base de datos: {e}"

    html = f"""
    <!doctype html>
    <html lang="es">
    <head>
      <meta charset="utf-8" />
      <title>Health del microservicio</title>
      <meta name="viewport" content="width=device-width, initial-scale=1" />
    </head>
    <body style="font-family:system-ui,-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;
                background:#020617;color:#e5e7eb;padding:24px;">
      <h1 style="font-size:22px;margin-bottom:8px;">Estado del microservicio</h1>
      <p style="margin-bottom:6px;">
        Estado: <span style="color:{color};font-weight:600;">{status_text}</span>
      </p>
      <p style="font-size:13px;">{detail}</p>
      <p style="margin-top:10px;font-size:13px;">
        Para el healthcheck automático de Docker se usa el endpoint JSON <code>/health</code>.
      </p>
      <p style="margin-top:6px;font-size:13px;">
        <a href="/" style="color:#38bdf8;text-decoration:none;">← Volver a la página principal</a>
      </p>
    </body>
    </html>
    """
    return HTMLResponse(html)
