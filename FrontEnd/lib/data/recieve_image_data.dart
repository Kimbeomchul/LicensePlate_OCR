import 'dart:convert';

class ReceiveImageData {
  String result;
  String path;
  ReceiveImageData({
    this.result,
    this.path,
  });

  Map<String, dynamic> toMap() {
    return {
      'result': result,
      'path': path,
    };
  }

  factory ReceiveImageData.fromMap(Map<String, dynamic> map) {
    if (map == null) return null;

    return ReceiveImageData(
      result: map['result'],
      path: map['path'],
    );
  }

  String toJson() => json.encode(toMap());

  factory ReceiveImageData.fromJson(String source) =>
      ReceiveImageData.fromMap(json.decode(source));
}
