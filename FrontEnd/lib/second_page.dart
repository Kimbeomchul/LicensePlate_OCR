import 'package:flutter/material.dart';

class SecondPage extends StatefulWidget {
  const SecondPage({Key key, String serverImageFileUrl})
      : _serverImage = serverImageFileUrl,
        super(key: key);

  @override
  _SecondPageState createState() => _SecondPageState();

  final _serverImage;
}


class _SecondPageState extends State<SecondPage> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        leading: IconButton(
          icon: Icon(
            Icons.arrow_back_ios,
            color: Colors.black,
          ),
          onPressed: () => Navigator.of(context).pop(),
        ),
        backgroundColor: Colors.transparent,
        elevation: 0.0,
      ),
      body: Center(
        child: Container(
          padding: EdgeInsets.all(30),
          child: Image.network(
            widget._serverImage,
            fit: BoxFit.cover,
          ),
        ),
      ),
    );
  }
}
