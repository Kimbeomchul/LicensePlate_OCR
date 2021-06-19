import 'dart:convert';

import 'package:dio/dio.dart';
import 'package:shared_preferences/shared_preferences.dart';
import 'package:test201210/data/recieve_image_data.dart';

const KEY_TOKEN = 'token';

class SendImageProvider {
  final Map<String, String> _headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
  };
  final String _baseUrl = 'http://127.0.0.1:8000/img';
  Future<Map> sendImage(SendImageData data) async {
    final token = await getSharedString(KEY_TOKEN);
    _headers['Authorization'] = 'Bearer $token';
    final _callUri = "/";
    final result = await multipart(
      _callUri,
      data.toMap(),
      data.image,
    );

    return result;
  }

  Future<String> getSharedString(String key) async {
    if (key != null) {
      SharedPreferences prefs = await SharedPreferences.getInstance();
      return prefs.getString(key);
    }
    return null;
  }

  Future<Map> multipart(
    String _path,
    Map map,
    String photo1Path,
  ) async {
    final token = await getSharedString(KEY_TOKEN);
    final formData = FormData.fromMap(map);

    if (photo1Path != null && photo1Path.isNotEmpty)
      formData.files.add(
        MapEntry(
          "image",
          MultipartFile.fromFileSync(photo1Path),
        ),
      );

    final response = await Dio().post(
      '$_baseUrl$_path',
      data: formData,
      options: Options(
        headers: {'Authorization': 'Bearer $token'},
      ),
    );

    print('dio response = ${response.toString()}');
    return response.data;
  }
}

class SendImageData {
  String image;
  SendImageData({
    this.image,
  });

  Map<String, dynamic> toMap() {
    return {
      'image': image,
    };
  }

  factory SendImageData.fromMap(Map<String, dynamic> map) {
    if (map == null) return null;

    return SendImageData(
      image: map['image'],
    );
  }

  String toJson() => json.encode(toMap());

  factory SendImageData.fromJson(String source) =>
      SendImageData.fromMap(json.decode(source));
}
