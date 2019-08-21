from app import app

if __name__ == '__main__':
    # port = int(os.environ.get('PORT', 8080))
    # app.run(app, host='0.0.0.0', port=port, debug=True, reloader=True, threaded=True)
    app.debug = True
    app.run(debug=True, threaded=True, reloader=True)
