from flask import jsonify, Blueprint

trips_routes_bp = Blueprint("trip_routes", __name__)


#criando rotas
@trips_routes_bp.route("/trips", methods = ["POST"])
def create_trip():
    return jsonify({"hello":"world"}),200

