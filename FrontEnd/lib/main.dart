import 'package:flutter/material.dart';
import 'package:flutter_easyloading/flutter_easyloading.dart';
import 'package:test201210/first_page.dart';

void main() async {
  runApp(
    new MyApp(),
  );
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'KindergartneDaebo',
      home: FirstPage(),
      builder: EasyLoading.init(),
    );
  }
}
