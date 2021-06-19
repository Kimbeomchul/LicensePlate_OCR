import 'package:test201210/provider/send_image_provider.dart';

import 'api_service.dart';

class ClassProvider {
  ApiService _api = ApiService();

  Future<SendImageData> getData() async {
    final _callUri = "/media/images/image_picker_EA2C6FD6-1D63-4D96-A49B-704D14254150-9919-00012CA18E9CB006.jpg";
    final response = await _api.get(_callUri);
    return SendImageData.fromMap(response);
  }
}
