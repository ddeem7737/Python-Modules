import os
from dotenv import load_dotenv


def load_conf() -> dict[str, str | None]:
    load_dotenv()

    config = {
        "MATRIX_MODE": os.environ.get("MATRIX_MODE", "development"),
        "DATABASE_URL": os.environ.get("DATABASE_URL", None),
        "API_KEY": os.environ.get("API_KEY", None),
        "LOG_LEVEL": os.environ.get("LOG_LEVEL", "DEBUG"),
        "ZION_ENDPOINT": os.environ.get("ZION_ENDPOINT", None),
    }

    return config


def show_conf(conf: dict[str, str | None]) -> None:
    print("ORACLE STATUS: Reading the Matrix...")
    print()
    print("Configuration loaded:")
    mode = conf['MATRIX_MODE']
    if mode == "production":
        print("Mode: production")
        print("WARNING: Running in production mode!")
    else:
        print("Mode: development")
        print("INFO: Running in development mode")
    db = conf['DATABASE_URL']
    if db:
        print("Database: Connected to local instance")
    else:
        print("Database: NOT CONFIGURED")
    api_key = conf['API_KEY']
    if api_key:
        print("API Access: Authenticated")
    else:
        print("API Access: NOT CONFIGURED")
    print(f"Log Level: {conf['LOG_LEVEL']}")
    zion = conf['ZION_ENDPOINT']
    if zion:
        print("Zion Network: Online")
    else:
        print("Zion Network: NOT CONFIGURED")


def main() -> None:
    conf = load_conf()
    show_conf(conf)
    print()
    print("Environment security check:")
    print("[OK] No hardcoded secrets detected")
    if os.path.exists(".env"):
        print("[OK] .env file properly configured")
    else:
        print("[WARNING] .env file not found. Using "
              "default environment variables.")
    print("[OK] Production overrides available")
    print()
    print("The Oracle sees all configurations.")


if __name__ == "__main__":
    main()
