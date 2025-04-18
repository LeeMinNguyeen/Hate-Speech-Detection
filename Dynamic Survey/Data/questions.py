from __future__ import annotations
from typing import Any

QUESTIONS: dict[str, Any] = {}

QUESTIONS['STANDARD'] = {
  "questions": [
    {
      "question": "Theo bạn, câu sau đây có thể hiện thái độ thù ghét/ mỉa mai trong một tình huống bất kỳ không? \"Giúp xứ người, đào lửa xứ mình\"",
      "answer": {
        "1": "Có",
        "2": "Không",
        "3": "Tôi không biết"
      }
    },
    {
      "question": "“Thua Tôn Bằng” có thể được dùng để mỉa mai những người đàn ông có tính gia trưởng cực đoan không?",
      "answer": {
        "1": "Có",
        "2": "Không",
        "3": "Tôi không biết"
      }
    },
    {
      "question": "“Không cần nói nữa Gobi, đủ lắm rồi” là câu đồng nghĩa với “im lặng”?",
      "answer": {
        "1": "Có",
        "2": "Không",
        "3": "Tôi không biết"
      }
    },
    {
      "question": "Bạn thấy cái này có 'đủ quao' chưa?",
      "answer": {
        "1": "Có",
        "2": "Không",
        "3": "Tôi không biết"
      }
    },
    {
      "question": "Nếu được chọn 1 người để hẹn hò, bạn có muốn hẹn hò với Jack không?",
      "answer": {
        "1": "Có",
        "2": "Không",
        "3": "Tôi không biết"
      }
    },
    {
      "question": "Khi nhìn lên bầu trời bầu trời, bạn có thấy 1 vì tinh tú không?",
      "answer": {
        "1": "Có",
        "2": "Không",
        "3": "Tôi không biết"
      }
    },
    {
      "question": "Bạn có thấy bạn quá ác không?",
      "answer": {
        "1": "Có",
        "2": "Không",
        "3": "Tôi không biết"
      }
    },
    {
      "question": "Bạn đã xem qua bộ phim ‘’Vườn sao kê’’ lần nào chưa?",
      "answer": {
        "1": "Có",
        "2": "Không",
        "3": "Tôi không biết"
      }
    },
    {
      "question": "Bạn có nghĩ Sigma boy là hình mẫu lý tưởng cho thanh niên không?",
      "answer": {
        "1": "Có",
        "2": "Không",
        "3": "Tôi không biết"
      }
    },
    {
      "question": "Bạn có đồng ý rằng diễn sâu quá là kỹ năng cần thiết trong công việc?",
      "answer": {
        "1": "Có",
        "2": "Không",
        "3": "Tôi không biết"
      }
    },
    {
      "question": "Bé Ba có phải là hình mẫu phụ nữ hiện đại không?",
      "answer": {
        "1": "Có",
        "2": "Không",
        "3": "Tôi không biết"
      }
    },
    {
      "question": "Kẹo rau củ có tốt cho sức khỏe hơn kẹo thường không?",
      "answer": {
        "1": "Có",
        "2": "Không",
        "3": "Tôi không biết"
      }
    },
    {
      "question": "Khi nhìn lên bầu trời, bạn có thấy một vì tinh tú không?",
      "answer": {
        "1": "Có",
        "2": "Không",
        "3": "Tôi không biết"
      }
    },
    {
      "question": "Nên cho trẻ em xem Skibidi Toilet để phát triển tư duy sáng tạo?",
      "answer": {
        "1": "Có",
        "2": "Không",
        "3": "Tôi không biết"
      }
    },
    {
      "question": "Bé Ba + Baby Three = Tuesday có phải là phương trình hạnh phúc?",
      "answer": {
        "1": "Có",
        "2": "Không",
        "3": "Tôi không biết"
      }
    },
    {
      "question": "Con gái hư có đáng bị gọi là 'Bé Ba' không?",
      "answer": {
        "1": "Có",
        "2": "Không",
        "3": "Tôi không biết"
      }
    },
    {
      "question": "Liệu 'Thị trấn đường' nên trở thành hình mẫu phát triển đô thị bền vững?",
      "answer": {
        "1": "Có",
        "2": "Không",
        "3": "Tôi không biết"
      }
    }
  ]
}

QUESTIONS["FIRST_GROUP"] = {
    "questions": [
    {
        "question": "Sarcasm thường được sử dụng như một công cụ để thể hiện sự thông minh/trí tuệ/khéo léo trong cộng đồng Gen Z",
        "answer": {
            "1": "Không đồng ý",
            "2": "Trung lập",
            "3": "Đồng ý"
        },
        "hypothesis": ["H4"]
    },
    {
        "question": "Khi sử dụng tài khoản ẩn danh (không có thông tin cá nhân thật), bạn có xu hướng sử dụng sarcasm tiêu cực hơn.",
        "answer": {
            "1": "Không đồng ý",
            "2": "Trung lập",
            "3": "Đồng ý"
        },
        "hypothesis": ["H7"]
    },
    {
        "question": "Bạn thường xuyên tiếp xúc với các nội dung mỉa mai/châm biếm từ nguồn nào?",
        "answer": {
            "1": "Các trang mạng xã hội (Tiktok, Facebook, Instagram,...)",
            "2": "Phim ảnh",
            "3": "Báo/ tạp chí",
            "4": "Bạn bè/ gia đình"
        },
        "hypothesis": ["H5", "H6"]
    },
    {
        "question": "Bạn dễ dàng nhận ra sarcasm hơn trong những trường hợp nào?",
        "answer": {
            "1": "Liên quan đến meme đang trending từ sự kiện xã hội hiện tại",
            "2": "Sử dụng ngôn ngữ Gen Z quen thuộc",
            "3": "Không liên quan đến yếu tố cụ thể nào"
        },
        "hypothesis": ["H5", "H6"]
    },
    {
        "question": "Bạn sử dụng lời nói mỉa mai/châm biếm trên mạng xã hội với tần suất như thế nào?",
        "answer": {
            "1": "Không bao giờ",
            "2": "Thỉnh thoảng",
            "3": "Rất thường xuyên"
        },
        "hypothesis": ["H3"]
    },
    {
        "question": "Bạn sử dụng lời nói mỉa mai/châm biếm trong giao tiếp hằng ngày với tần suất như thế nào?",
        "answer": {
            "1": "Không bao giờ",
            "2": "Thỉnh thoảng",
            "3": "Rất thường xuyên"
        },
        "hypothesis": ["H3"]
    },
    {
        "question": "Trong bối cảnh một nội dung video gây tranh cãi về người có ảnh hưởng trên mạng xã hội liên quan đến hành vi cá nhân không phù hợp với chuẩn mực đạo đức, xuất hiện bình luận như sau: 'Có người cứu J97 rồi sao :))'",
        "answer": {
            "1": "Tiêu cực (thể hiện thái độ phản đối, chỉ trích, mỉa mai hoặc châm biếm tiêu cực)",
            "2": "Trung tính (không biểu lộ rõ thái độ tích cực hay tiêu cực)",
            "3": "Tích cực/Hài hước (mang tính hài hước, gây cười hoặc thể hiện thái độ tích cực)"
        },
        "hypothesis": ["Hiểu biết", "H5"]
    },
    {
        "question": "Theo bạn, từ ngữ sau đây thể hiện sắc thái như thế nào? 'Bố mẹ ra đường chắc tự hào về con lắm'",
        "answer": {
            "1": "Tiêu cực (thể hiện thái độ phản đối, chỉ trích, mỉa mai hoặc châm biếm tiêu cực)",
            "2": "Trung tính (không biểu lộ rõ thái độ tích cực hay tiêu cực)",
            "3": "Tích cực/Hài hước (mang tính hài hước, gây cười hoặc thể hiện thái độ tích cực)"
        },
        "hypothesis": ["Hiểu biết", "H5"]
    },
    {
        "question": "Theo bạn, cụm từ 'Khó chịu vô cùng' được cho là có sắc thái chỉ trích/ mỉa mai trong trường hợp nào?",
        "answer": {
            "1": "Khi đây là bình luận dưới video về hành vi vứt rác bừa bãi ở khu vực công cộng",
            "2": "Khi đây là bình luận dưới video chia sẻ khoảnh khắc dễ thương của một cặp tình nhân",
            "3": "Khi đây là bình luận dưới video về thông tin dự báo thời tiết nắng nóng tại Thành phố HCM"
        },
        "hypothesis": ["Hiểu biết"]
    },
    {
        "question": "Khi bạn lướt mạng xã hội (Facebook, TikTok, v.v), bạn thường gặp nhiều nhất loại nội dung nào sau đây?",
        "answer": {
            "1": "Những câu nói mang tính đùa cợt, đá xéo hoặc mỉa mai người khác",
            "2": "Những câu chửi thẳng, xúc phạm hoặc thù ghét công khai",
            "3": "Những câu nói vô nghĩa, chỉ để gây cười mà không có nội dung sâu xa"
        },
        "hypothesis": ["H1"]
    },
    {
        "question": "Các câu nói mỉa mai trong những hội nhóm riêng (VD: fanclub, group bạn bè) sẽ khó hiểu hơn đối với người ngoài nhóm.",
        "answer": {
            "1": "Không đồng ý",
            "2": "Trung lập",
            "3": "Đồng ý"
        },
        "hypothesis": ["H8"]
    },
    {
        "question": "Theo bạn, những câu mỉa mai (sarcasm) trên mạng xã hội có thể khiến người khác:",
        "answer": {
            "1": "Cảm thấy bị xúc phạm nhưng khó chỉ trích lại vì nó nghe có vẻ hài hước",
            "2": "Dễ hiểu nhầm là nói đùa dù thực chất là công kích",
            "3": "Giải trí và nhẹ nhàng hóa vấn đề, không nghiêm trọng",
            "4": "Không để lại ấn tượng gì, dễ lướt qua"
        },
        "hypothesis": ["H2"]
    },
    {
        "question": "Theo bạn, yếu tố nào ảnh hưởng nhiều nhất đến khả năng hiểu sarcasm (châm biếm) của Gen Z?",
        "answer": {
            "1": "Câu hỏi mở"
        },
        "hypothesis": ["H6"]
    }
]
}

QUESTIONS["SECOND_GROUP"] = {
    "questions": [
        {
            "question": "Khi bạn lướt mạng xã hội (Facebook, TikTok, v.v), bạn thường gặp nhiều nhất loại nội dung nào sau đây?",
            "answer": {
                "1": "Những câu nói mang tính đùa cợt, đá xéo hoặc mỉa mai người khác",
                "2": "Những câu chửi thẳng, xúc phạm hoặc thù ghét công khai",
                "3": "Những câu nói vô nghĩa, không có nội dung sâu xa",
            },
            "hypothesis": ["H1"]
        },
        {
            "question": "Theo bạn, những câu mỉa mai (sarcasm) trên mạng xã hội có thể khiến người khác:",
            "answer": {
                "1": "Cảm thấy bị xúc phạm nhưng khó chỉ trích lại vì nó nghe có vẻ hài hước",
                "2": "Dễ hiểu nhầm là nói đùa dù thực chất là công kích",
                "3": "Giải trí và nhẹ nhàng hóa vấn đề, không nghiêm trọng",
                "4": "Không để lại ấn tượng gì, dễ lướt qua"
            },
            "hypothesis": ["H2"]
        },
        {
            "question": "Bạn có thường sử dụng các câu nói mỉa mai, đá xéo (sarcasm) khi đăng bài hoặc bình luận trên mạng xã hội không?",
            "answer": {
                "1": "Có, thường xuyên",
                "2": "Thỉnh thoảng",
                "3": "Hiếm khi",
                "4": "Không bao giờ"
            },
            "hypothesis": ["H6"]
        },
        {
            "question": "Bạn nghĩ vì sao một số người thích dùng sarcasm trên mạng xã hội?",
            "answer": {
                "1": "Vì nó nghe “thâm thúy” và thể hiện sự thông minh",
                "2": "Để né tránh bị phản ứng trực tiếp",
                "3": "Vì thấy người khác cũng làm vậy",
                "4": "Vì muốn gây cười hoặc tạo tương tác",
                "5": "Không rõ lý do"
            },
            "hypothesis": ["H8"]
        },
        {
            "question": "Bạn có dễ dàng hiểu các câu nói mỉa mai khi chúng gắn với xu hướng mạng xã hội, meme hoặc sự kiện nổi bật không?",
            "answer": {
                "1": "Dễ hiểu hơn nhiều",
                "2": "Cũng như bình thường",
                "3": "Khó hiểu hơn",
                "4": "Không rõ"
            },
            "hypothesis": ["H10a"]
        },
        {
            "question": "Theo bạn, điều gì khiến một người dễ hiểu sarcasm hơn?",
            "answer": {
                "1": "Xem nhiều nội dung mạng xã hội",
                "2": "Có vốn từ ngữ và hiểu cách chơi chữ",
                "3": "Từng trải với nhiều tình huống xã hội",
                "4": "Là người hài hước",
                "5": "Không biết nữa"
            },
            "hypothesis": ["H10b"]
        },
        {
            "question": "Bạn nghĩ những tài khoản ẩn danh/không có ảnh thật trên mạng có xu hướng sử dụng các bình luận mỉa mai/độc hại:",
            "answer": {
                "1": "Thường xuyên hơn tài khoản thật",
                "2": "Ít hơn tài khoản thật",
                "3": "Không khác biệt nhiều",
                "4": "Không rõ"
            },
            "hypothesis": ["H14"]
        },
        {
            "question": "Bạn có từng đọc một bình luận hoặc câu nói mỉa mai mà người khác hiểu ngay, còn bạn thì không hiểu ý hoặc hiểu sai ý không?",
            "answer": {
                "1": "Có, khá thường xuyên",
                "2": "Có, nhưng ít",
                "3": "Gần như không",
                "4": "Không nhớ"
            },
            "hypothesis": ["H19"]
        },
        {
            "question": "Bạn có nghĩ rằng các câu nói mỉa mai trong những hội nhóm riêng (VD: fanclub, group bạn bè) sẽ khó hiểu hơn đối với người ngoài nhóm?",
            "answer": {
                "1": "Có, vì thường có “code” hoặc ngôn ngữ riêng",
                "2": "Không, ai cũng có thể hiểu nếu theo dõi",
                "3": "Tùy trường hợp",
                "4": "Không rõ"
            },
            "hypothesis": ["H19"]
        },
        {
            "question": "Một streamer đình đám mở livestream giải thích về loạt tin đồn, bốc phốt và những lời bôi nhọ nhắm vào mình thời gian qua. Càng thanh minh, anh ta lại vô tình thốt ra những câu nói gây hại cho chính bản thân. Và thế là, cộng đồng mạng nhanh chóng 'tặng' anh loạt bình luận 'Đồng Jack nay xuống giá rồi ha'.",
            "answer": {
                "1": "Tiêu cực (thể hiện thái độ phản đối, chỉ trích, mỉa mai hoặc châm biếm tiêu cực)",
                "2": "Trung tính (không biểu lộ rõ thái độ tích cực hay tiêu cực)",
                "3": "Tích cực/Hài hước (mang tính hài hước, gây cười hoặc thể hiện thái độ tích cực)"
            },
            "hypothesis": ["Hiểu biết"]
        },
        {
            "question": "Theo bạn cụm từ ''Xịt keo'' thể hiện sắc thái như nào?",
            "answer": {
                "1": "Tiêu cực (thể hiện thái độ phản đối, chỉ trích, mỉa mai hoặc châm biếm tiêu cực)",
                "2": "Trung tính (không biểu lộ rõ thái độ tích cực hay tiêu cực)",
                "3": "Tích cực/Hài hước (mang tính hài hước, gây cười hoặc thể hiện thái độ tích cực)"
            },
            "hypothesis": ["Hiểu biết"]
        },
        {
            "question": "Trên các trang thông tin chính thức của các báo chính thống đăng tải bài viết về vụ việc công ty kẹo K có hành vi kinh doanh thiếu minh bạch, ảnh hưởng đến quyền lợi người tiêu dùng. Đáng chú ý, công ty này từng được quảng bá rộng rãi bởi bà HDM, ông QL và đặc biệt có sự liên quan đến hoa hậu T. Sau khi thông tin được đăng tải, hoa hậu T nhanh chóng lên tiếng phủ nhận trách nhiệm, khẳng định mình chỉ đóng vai trò KOL/KOC chứ không tham gia điều hành. Tuy nhiên, nhiều cư dân mạng tỏ ra hoài nghi, thể hiện qua hàng loạt bình luận như: 'Đấy, tôi nói rồi, nhìn mặt là biết ngay, chỉ là trước đây không nói ra thôi'.",
            "answer": {
                "1": "Tiêu cực (thể hiện thái độ phản đối, chỉ trích, mỉa mai hoặc châm biếm tiêu cực)",
                "2": "Trung tính (không biểu lộ rõ thái độ tích cực hay tiêu cực)",
                "3": "Tích cực/Hài hước (mang tính hài hước, gây cười hoặc thể hiện thái độ tích cực)"
            },
            "hypothesis": ["Hiểu biết"]
        }
    ]
}