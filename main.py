from app import create_app
import py_eureka_client.eureka_client as eureka_client

# eureka_client.init(eureka_server="https://eureka-service-ufps.herokuapp.com/eureka",
#                    app_name="registermicroservice")
app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
