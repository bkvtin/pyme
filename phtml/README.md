# `phtml` 

## what-is-it-?
parse html-tag and collect the url, title, author and date

## how-to-build-?
```sh
$ docker build -t phtml .
```

## how-to-run-?
```sh
$ docker run phtml
```

## example-output-
```sh
URL,Title,Author,Date
https://www.thesaigontimes.vn/121624/Cuoc-cach-mang-dau-khi-da-phien.html,Cuộc cách mạng dầu khí đá phiến,Trần Hữu Hiếu (*),Thứ Sáu,  24/10/2014, 19:25 
https://www.thesaigontimes.vn/274113/bao-giay-van-thu-vi.html,Báo giấy vẫn thú vị!,Lê Ngọc Quỳnh,Thứ Năm,  21/6/2018, 10:20 
https://www.thesaigontimes.vn/274112/tiep-tuc-da-cat-giam-thu-tuc-hanh-chinh.html,Tiếp tục đà cắt giảm thủ tục hành chính,Nguyễn Đức Nguyên,Thứ Hai,  25/6/2018, 11:21 
https://www.thesaigontimes.vn/274111/con-bao-nhieu-nhom-loi-ich.html,Còn bao nhiêu nhóm lợi ích?,Ngọc Bình,Thứ Hai,  25/6/2018, 11:21 
https://www.thesaigontimes.vn/274105/phe-lieu-va-logistics.html,Phế liệu và logistics,Đặng Dương,Chủ Nhật,  24/6/2018, 09:33 
https://www.thesaigontimes.vn/274104/tim-cach-chan-hang-rac-cong-nghiep-do-ve-viet-nam.html,Tìm cách chặn hàng rác công nghiệp đổ về Việt Nam,Minh Tâm,Chủ Nhật,  24/6/2018, 09:33 
```
