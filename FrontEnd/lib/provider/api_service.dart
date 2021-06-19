import 'dart:convert';
import 'dart:io';
import 'package:http/http.dart' as http;
import 'package:shared_preferences/shared_preferences.dart';

const KEY_TOKEN = 'token';

class ApiService {
  final String _baseUrl = 'http://127.0.0.1:8000/img';

  final Map<String, String> _headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
  };

  // var client = new http.Client();
  Future<dynamic> get(String _path) async {
    final token = await getSharedString(KEY_TOKEN);
    print(token);
    _headers['Authorization'] = 'Bearer $token';

    print('Api get : url $_path start.');
    var responseJson;
    try {
      final response = await http
          .get(Uri.encodeFull('$_baseUrl$_path'), headers: _headers)
          .timeout(Duration(seconds: 10));
      print('Api get : url $_path  done.');
      responseJson = _response(response);
    } on SocketException {}
    return responseJson;
  }

  dynamic _response(http.Response response) {
    switch (response.statusCode) {
      case 200:
      case 201:
        var responseJson = json.decode(response.body.toString());
        return responseJson;
      case 400:

      case 401:
      case 403:

        
      case 500:

      default:
    }
  }

  Future<String> getSharedString(String key) async {
    if (key != null) {
      SharedPreferences prefs = await SharedPreferences.getInstance();
      return prefs.getString(key);
    }
    return null;
  }
}
