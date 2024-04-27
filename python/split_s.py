# -*- coding: utf-8 -*-
import jieba
import jieba.posseg as pseg


def split_Chinese(text):
    seg_list = jieba.cut(text)
    # result = ' '.join(seg_list)
    return seg_list

def split_history(text_list):
    content_list = []
    for i,j in enumerate(text_list):
        if i % 2 == 0:
            content_list.append(j['message']['content'])
    words = []
    words1 = []
    for i in content_list:
        print(i)
        for word in split_Chinese(i):
            words.append(word)
        for p in pseg.cut(i):
            words1.append(p)
    return words

test1 = {
    "历史内容":[
        {
            "fileItems": [],
            "message": {
                "chat_id": "3d9080b5-2105-43ea-a6fc-20071bd5e57b",
                "content": "操作系统是什么",
                "created_at": "2024-04-19T10:19:51.962949+00:00",
                "id": "cf21e8ae-6257-4910-b875-af6ebb6db42a",
                "image_paths": [],
                "model": "gpt-4-turbo-preview",
                "role": "user",
                "sequence_number": 0,
                "updated_at": "2024-04-19T10:19:51.986351+00:00",
                "user_id": "af6df030-2f42-4fc7-adb6-2d46623fb7a1"
            }
        },{
            "fileItems": [],
            "message": {
                "chat_id": "3d9080b5-2105-43ea-a6fc-20071bd5e57b",
                "content": "操作系统的定义",
                "created_at": "2024-04-19T10:19:51.962949+00:00",
                "id": "cf21e8ae-6257-4910-b875-af6ebb6db42a",
                "image_paths": [],
                "model": "gpt-4-turbo-preview",
                "role": "user",
                "sequence_number": 0,
                "updated_at": "2024-04-19T10:19:51.986351+00:00",
                "user_id": "af6df030-2f42-4fc7-adb6-2d46623fb7a1"
            }
        },
        {
            "fileItems": [],
            "message": {
                "chat_id": "3d9080b5-2105-43ea-a6fc-20071bd5e57b",
                "content": "操作系统的定义",
                "created_at": "2024-04-19T10:19:51.962949+00:00",
                "id": "cf21e8ae-6257-4910-b875-af6ebb6db42a",
                "image_paths": [],
                "model": "gpt-4-turbo-preview",
                "role": "user",
                "sequence_number": 0,
                "updated_at": "2024-04-19T10:19:51.986351+00:00",
                "user_id": "af6df030-2f42-4fc7-adb6-2d46623fb7a1"
            }
        },{},{
            "fileItems": [],
            "message": {
                "chat_id": "3d9080b5-2105-43ea-a6fc-20071bd5e57b",
                "content": "嵌入式操作系统是操作系统",
                "created_at": "2024-04-19T10:19:51.962949+00:00",
                "id": "cf21e8ae-6257-4910-b875-af6ebb6db42a",
                "image_paths": [],
                "model": "gpt-4-turbo-preview",
                "role": "user",
                "sequence_number": 0,
                "updated_at": "2024-04-19T10:19:51.986351+00:00",
                "user_id": "af6df030-2f42-4fc7-adb6-2d46623fb7a1"
            }
        }

    ]
    }
# w1,w2 = split_history(test1["历史内容"])
# print(w2)
# print(split_Chinese('操作系统是什么'))