import random

who = ["một con khỉ","hoàng đế","Sư tử","một người đàn ông tham lam"]

print(who)

a = input("Mời nhập vào số của nhân vật bạn muốn chọn :")

when = ["Một ngày nọ","Ngày xửa ngày xưa"]
where = ["vương quốc xa xôi","thị trấn nhỏ","cánh rừng già"]

name = input("Hãy nhập tên nhân vật:")



if a == '0':
    print(f"{random.choice(when)}, có một con khỉ tên {name} sống ở một {random.choice(when)} lớn và làm bạn với một con cá sấu sống ở dòng sông gần đó.Mỗi ngày, {name} sẽ hái những quả táo ngon ở trên cây và đem tặng bạn cá sấu."
            + f"Nhận được quà từ {name}, cá sấu đem về và ăn chung với vợ mình. Vợ của cá sấu là một người rất tham ăn và muốn ăn cả trái tim của chú khỉ"
            + "Nghe mong muốn đó của vợ, cá sấu rất băn khoăn nhưng vẫn làm theo ý vợ."
            + "Cá sấu đã mời khỉ ngồi trên lưng mình để đưa đi tham quan dòng sông nhưng thật ra nó có ý định giết khỉ và lấy quả tim khi bơi đến giữa dòng. Khi khỉ biết được mưu đồ xấu xa của cá sấu, nó đã nhanh trí nói với cá sấu rằng mình để quả tim ở trên cây. Nếu muốn lấy thì hãy chở nó quay lại. Cá sấu tin lời, chở khỉ quay trở lại để lấy quả tim. Thế nhưng, khi đến nơi, khỉ đã thoăn thoắt trèo lên cây và chẳng mấy chốc biến mất. Và thế là, kế hoạch của cá sấu đã hoàn toàn thất bại")
    print("\nÝ nghĩa của câu chuyện: Khi gặp tình huống khó khăn, con hãy bình tĩnh và sử dụng trí thông minh của mình để vượt qua điều đó.")
if a == '1':
    print(f'{random.choice(when)}, {name} - Hoàng đế của {random.choice(when)}, đã hỏi các quan cận thần của mình một câu hỏi lạ khiến mọi người vô cùng ngạc nhiên'
            + 'Không ai biết phải trả lời như thế nào cho đức vua cả. Ngay lúc đó, Birbal, một vị quan được xem là người thông minh nhất ở đất nước này, bước vào và hỏi các quan tại sao trông họ lại lo lắng vậy.Các quan kể lại với ông rằng, hoàng đế đã hỏi một câu hỏi mà không ai biết trả lời thế nào cả. Đó là: “Có bao nhiêu con quạ trong thành?"\n'
            + f'Sau khi nghe xong, ông nở một nụ cười và trả lời: “Thưa bệ hạ, thần biết câu trả lời. Có 50.589 con quạ trong thành”. Mọi người sửng sốt trước câu trả lời đó, kể cả hoàng đế nên {name} đã hỏi lại ông: “Tại sao ngươi lại chắc chắn như vậy?”.\n'
          +'Birbal thưa: “Thưa bệ hạ, xin hãy sai một tên lính ngồi đếm số quạ trong thành. Nếu có nhiều hơn số quạ mà thần nói, điều đó có nghĩa là họ hàng của chúng ở nơi khác đến thăm. Nếu có ít hơn thì có nghĩa là một số con đã đi thăm họ hàng của chúng ở nơi khác”. Hoàng đế Akbar cảm thấy rất hài lòng với câu trả lời dí dỏm của Birbal.'
          )


    print("\nÝ nghĩa của câu chuyện: Khi nói ra một điều gì đó, con phải có cách lý giải rõ ràng tại sao con nói như vậy.")

if a == '2':
    print(f"{random.choice(when)}, một con Sư tử tên {name} đang ngủ trong {random.choice()}. Chuột chạy qua trên người sư tử làm nó chòang tỉnh và tóm được chuột. Chuột lên tiếng van xin sư tử tha mạng.\n"
           +'Chuột nói:\n'
           + '- Nếu ông thả cháu ra, cháu sẽ làm điều tốt cho ông.\n'
           +f'{name} bật cười vì chuột nhắt hứa sẽ làm điều tốt cho nó, nhưng cũng thả chuột ra.'
           +'Về sau những người thợ săn tóm được sư tử và lấy dây trói sư tử vào thân cây.'+'Chuột nhắt nghe tiếng sư tử gầm, chạy đến cắn đứt dây thừng và nói:\n'
           +'- Ông có còn nhớ là khi đó ông cười, ông không nghĩ là chuột nhắt cháu lại có thể làm cho ông một điều tốt nào. Còn bây giờ ông thấy đó, có khi chuột nhắt cũng làm được việc lắm chứ.')

    print("\nBài học rút ra:\n"

            +"Làm việc tốt thì không bao giờ thiệt")

if a == '3':
    print(f"{random.choice(when)} , có một người đàn ông tên {name} tham lam sống ở {random.choice(where)} nọ."
          +'Người đàn ông này vô cùng giàu và có một niềm say mê đặc biệt với vàng cùng những thứ lạ mắt. Mặt khác, ông ta cũng rất yêu thương con gái duy nhất của mình hơn bất cứ điều gì trên đời.'
          +'\nVào một ngày khi đang đi làm việc, người đàn ông tình cờ gặp một nàng tiên khi mái tóc của nàng tiên nữ ấy đang mắc kẹt vào một nhánh cây. Không suy nghĩ nhiều, người đàn ông liền lao đến và giúp đỡ nàng tiên.'
          +'\nNgay sau đó, lòng tham nổi dậy, ông ta lập tức yêu cầu nàng tiên đáp lại sự giúp đỡ bằng việc ban cho ông một điều ước. Người đàn ông ước rằng tất cả những gì ông ta chạm vào đều sẽ hóa thành vàng. Vị tiên nhận lời.'
          +'\nSau khi có được điều ước, người đàn ông tham lam vội vã về nhà để cho vợ và con thấy điều kỳ diệu mà mình có được. Khi ông ta vừa đến nhà, cô con gái yêu chạy ra đón và vô tình chạm vào tay cha. Ngay lập tức, toàn thân cô hóa thành vàng. Người đàn ông lúc này vô cùng hối tiếc về ước muốn sai lầm kia và dành quãng đời còn lại để tìm kiếm nàng tiên đã ban cho mình điều ước đó.')
    
    print('\nBài học rút ra:'

            '\nBàn tay vàng là truyện ngắn thiếu nhi hay giúp bé hiểu lòng tham vô đáy sẽ dẫn con người ta đến những kết cục bi thương.')
















