import 'dart:io';

import 'package:flutter/material.dart';
import 'package:flutter_easyloading/flutter_easyloading.dart';
import 'package:image_picker/image_picker.dart';
import 'package:test201210/data/recieve_image_data.dart';
import 'package:test201210/provider/class_provider.dart';
import 'package:test201210/second_page.dart';
import 'package:test201210/provider/send_image_provider.dart';

class FirstPage extends StatefulWidget {
  @override
  _FirstPageState createState() => _FirstPageState();
}

class _FirstPageState extends State<FirstPage> {
  File _imageFile;
  String _serverImageFileUrl;

  final ImagePicker picker = ImagePicker();

  @override
  void initState() {
    super.initState();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: new AppBar(
        backgroundColor: Colors.transparent,
        elevation: 0.0,
      ),
      body: _body(),
    );
  }

  _body() {
    Size size = MediaQuery.of(context).size;
    return Container(
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.center,
        children: [
          Expanded(
            child: Container(
              width: size.width,
              child: getImageContainer(),
            ),
          ),
          FlatButton(
            onPressed: () async {
              await getImage();
            },
            child: Text('사진선택'),
          ),
          FlatButton(
            onPressed: () async {
              await sendImageToServer();
            },
            child: Text('사진 전송'),
          ),
          SizedBox(
            height: 20,
          ),
        ],
      ),
    );
  }

  Widget getImageContainer() {
    if (_imageFile == null)
      return SizedBox.shrink();
    else {
      return Image.file(
        _imageFile,
        fit: BoxFit.cover,
      );
    }
  }

  Future<void> getImage() async {
    final pickedFile = await picker.getImage(source: ImageSource.gallery);
    setState(() {
      if (pickedFile != null) {
        _imageFile = File(pickedFile.path);
      } else {
        print('no image');
      }
    });
  }

  Future<void> sendImageToServer() async {
    await EasyLoading.show(
      status: 'uploading...',
      maskType: EasyLoadingMaskType.black,
    );
    SendImageData sendImageData = new SendImageData(
      image: _imageFile.path,
    );

    SendImageProvider provider = new SendImageProvider();

    await provider.sendImage(sendImageData).then(
      (value) {
        EasyLoading.dismiss();
        if (value['result'] == "True") {
          _serverImageFileUrl = 'http://127.0.0.1:8000' + value['path']; // PATH
          print('success');

          Navigator.of(context).push(
            MaterialPageRoute(
                builder: (context) =>
                    SecondPage(serverImageFileUrl: _serverImageFileUrl)),
          );
        } else {
          print('fail');
          Scaffold.of(context)
              .showSnackBar(SnackBar(content: Text("서버와의 통신에 문제가 발생했습니다.")));
        }
      },
    );
  }
}
