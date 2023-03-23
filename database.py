from sqlalchemy import create_engine, text

database_connection_string = 'mysql+pymysql://jdqaoncdc08l4zofd7e1:pscale_pw_vagijm8HbSVyyYJIr2n3aPjRHHKUwGUB9lkqnpPWEZK@ap-south.connect.psdb.cloud/kaifcareers'

engine = create_engine(database_connection_string,
                       connect_args={
                         "ssl": {
                           "ssl_ca": "/etc/ssl/cert.pem"
                         }
                       })

def derive_jobs():
  with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM jobs"))
    jobs = []
    for row in result.all():
      jobs.append(dict(row._mapping))
    return jobs
  