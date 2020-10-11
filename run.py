from flaskblog import create_app

app = create_app()

# Use python script to open in localhost instead of opening through flask
if __name__ == '__main__':
    app.run(debug=True)