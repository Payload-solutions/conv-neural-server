from app import create_app
import os


if __name__ == "__main__":
    print("VERIFYING......")
    print(os.system("ls -la"))
    app = create_app()
    app.run(host="0.0.0.0", port=5000)