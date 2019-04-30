"""
Simple Time Server
Microservice that provides the current Unix (epoch) time
"""

import os
import time
from flask import Flask

app = Flask(__name__)

@app.route("/")
def get_time():
    """Get current Unix (epoch) time"""
    now = int(time.time())
    return str(now)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6738))
    app.run(host="0.0.0.0", port=port)
