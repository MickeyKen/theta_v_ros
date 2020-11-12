#### Theta Vからwifi経由で画像を取得して，ROSの画像トピックに変換するパッケージ
##### 実行方法
    $ node main.js
    $ rosrun theta_v_ros theta_image.py

##### NOTE
このノードがパブリッシュするトピックの名前は`/camera/color/image_raw`です






#### [openvino](https://github.com/intel/ros_openvino_toolkit)で顔の向きを推定する

    $ roslaunch vino_launch pipeline_people_oss.launch

##### NOTE
- [ros_openvino_toolkit/vino_launch/param/pipeline_people_oss.yaml](https://github.com/intel/ros_openvino_toolkit/blob/master/vino_launch/param/pipeline_people_oss.yaml) の `StandardCamera` を `RealSenseCameraTopic` に変更しておく
- pipeline_people_oss が subscribe するトピック名は `/camera/color/image_raw` です
