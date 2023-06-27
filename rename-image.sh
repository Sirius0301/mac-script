rm -f *.jpg
mv /Users/shimin/Library/Containers/com.tencent.xinWeChat/Data/Library/"Application Support"/com.tencent.xinWeChat/2.0b4.0.9/1b41bee987f1a82c120223a43d259ea4/Message/MessageTemp/0acce192b538c94367c56b21288630ac/Image/* /Users/shimin/Desktop/wechat-image/
rm -f *thumb.*
rm -f *hd
cd /Users/shimin/Desktop/wechat-image/
find . ! -type d -mtime +7 -delete
python /Users/shimin/opt/mac-script/rename-image.py