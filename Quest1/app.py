{
    "version": 2,
    "builds": [
      {
        "src": "app/app.py",
        "use": "@vercel/python"
      }
    ],
    "routes": [
      {
        "src": "/(.*)",
        "dest": "app/app.py"
      }
    ]
}