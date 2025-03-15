import sentry_sdk

sentry_sdk.init(
    dsn="https://673e5ab0c1ddaa2d972f868443c260a8@o4508981080555520.ingest.de.sentry.io/4508981084815440",
    # Add data like request headers and IP for users,
    # see https://docs.sentry.io/platforms/python/data-management/data-collected/ for more info
    send_default_pii=True,
    environment="development"
    release="1.0"

)
if __name__ == "__main__":
    division_zero = 1 /0
    