import torch

def driver_detection(img):
    
    model = torch.hub.load('ultralytics/yolov5', 'custom', path='best_YOLO_test.pt') #force_reload=True
    model.eval()

    drivers_dict = {
            1:'глаза открыты рот закрыт',
            2:'глаза октрыты рот широко улыбается',
            3:'глаза открыты рот зевает',
            4:'глаза открыты, рот прикрыт рукой',
            5:'глаза закрыты рот закрыт',
            6:'глаза закрыты рот зевает',
            7:'глаза закрыты рот прикрыт рукой',
            8:'человек в черных солнцезащитных очках'
        }

    # Inference
    results = model(img)

    # Results
    # results.show()
    # получаем лист из 2 значений: на первом месте - класс, на втором - вероятность принадлежности.
    list_with_class_and_prob = results.crop()[0]['label'].split()

    #обращаемся к словарю по классу, который задетектила модель
    get_class = drivers_dict.get(int(list_with_class_and_prob[0]))

    #записываем ответ с вероятностью принадлежности к классу
    reply_msg = f'C вероятностью {list_with_class_and_prob[1]} {get_class}'
    print(reply_msg)

    return reply_msg

driver_detection('test.jpg')