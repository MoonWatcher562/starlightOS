import uvicorn
import backend.app as backend

## Keep app in global
app = backend.app

def main():
    ## Run the backend
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)


if __name__ == "__main__":
    main()
