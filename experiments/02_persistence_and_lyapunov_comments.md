# Nhận xét notebook 02 - Persistence and Lyapunov

Notebook này tái hiện các kết quả ở Section 3 của paper: coexistence, uniform persistence và kiểm tra trực quan các hàm Lyapunov dùng để chứng minh ổn định toàn cục của các hệ con.

## Experiment 1 - Coexistence equilibrium P3

Thí nghiệm này chọn tham số sao cho tồn tại cân bằng nội:

```text
P3 = (S3, x3, y3, z3)
```

trong đó cả bốn thành phần đều dương.

Hình time series cho thấy `S(t), x(t), y(t), z(t)` không tiến về 0 mà dao động/hội tụ trong miền dương. Sau giai đoạn quá độ ban đầu, các biến duy trì giá trị dương lâu dài. Điều này minh họa kết quả coexistence của hệ.

Hình phase portrait 3D trong không gian `(x,y,z)` cho thấy quỹ đạo đi vào vùng hấp dẫn quanh cân bằng nội `P3`. Điểm đỏ biểu diễn cân bằng nội, nơi prey, predator bậc 1 và predator bậc 2 cùng tồn tại.

Kết quả này tương ứng với Theorem 3.4: khi các điểm cân bằng biên không hút nghiệm nội và hệ là dissipative, nghiệm xuất phát trong miền dương sẽ không bị kéo về biên tuyệt chủng.

Ý nghĩa sinh học: cả ba bậc trong chuỗi thức ăn đều có thể cùng tồn tại trong chemostat khi mỗi loài có đủ khả năng duy trì trước tốc độ loại bỏ.

## Experiment 2 - Uniform persistence from many initial conditions

Thí nghiệm này chạy nhiều điều kiện đầu dương khác nhau và vẽ:

```text
min{x(t), y(t), z(t)}
```

Đường này biểu diễn mật độ nhỏ nhất trong ba quần thể sinh vật tại mỗi thời điểm. Nếu đường này không tiến về 0 sau quá độ, điều đó cho thấy không quần thể nào bị tuyệt chủng.

Các hình thu được cho thấy dù điều kiện đầu khác nhau, sau một khoảng thời gian ban đầu, các nghiệm đều nằm cách xa trục tuyệt chủng. Đây là minh họa số cho uniform persistence.

Kết quả này gắn trực tiếp với Theorem 3.4. Theorem 3.4 không chỉ nói rằng tồn tại cân bằng nội, mà còn nói rằng nghiệm bắt đầu trong miền dương sẽ không tiến sát biên `x=0`, `y=0` hoặc `z=0`.

Ý nghĩa sinh học: coexistence không phải hiện tượng chỉ xảy ra với một điều kiện đầu đặc biệt. Trong miền tham số này, nhiều trạng thái ban đầu khác nhau đều dẫn đến sự tồn tại lâu dài của toàn bộ chuỗi thức ăn.

## Experiment 3 - Lyapunov function for P1

Thí nghiệm này xét hàm Lyapunov cho hệ con `(S,x)` quanh cân bằng:

```text
P1 = (S1, x1, 0, 0)
```

Hàm được vẽ có dạng:

```text
V(S,x) = 1/2 (S-S1)^2 + 1/2 (x-x1)^2
```

Hình `V(t)` giảm dần về gần 0 cho thấy khoảng cách năng lượng giữa nghiệm và cân bằng `P1` giảm theo thời gian. Điều này minh họa cách paper dùng hàm Lyapunov để chứng minh ổn định toàn cục trong hệ con.

Kết quả tương ứng với Theorem 3.1. Khi các điều kiện xác định âm của đạo hàm Lyapunov được thỏa mãn, nghiệm trong mặt phẳng `(S,x)` hội tụ về `P1`.

Ý nghĩa sinh học: trong trường hợp predator không thể tồn tại, hệ nutrient-prey tự điều chỉnh về một trạng thái ổn định duy nhất, không phụ thuộc mạnh vào điều kiện ban đầu.

## Experiment 4 - Lyapunov function for P2

Thí nghiệm này xét hàm Lyapunov cho hệ con `(S,x,y)` quanh cân bằng:

```text
P2 = (S2, x2, y2, 0)
```

Hàm Lyapunov trong notebook có dạng entropy cho nutrient và dạng bình phương cho prey, predator 1:

```text
W(S,x,y) = S - S2 - S2 ln(S/S2)
           + 1/2 (x-x2)^2
           + 1/2 (y-y2)^2
```

Hình `W(t)` giảm về gần 0, cho thấy nghiệm tiến gần đến cân bằng `P2`. Dạng `S - S2 - S2 ln(S/S2)` luôn không âm khi `S>0`, nên phù hợp để đo sai lệch nồng độ dinh dưỡng trong hệ dương.

Kết quả này tương ứng với Theorem 3.2. Nó minh họa rằng `P2` có thể ổn định toàn cục trong hệ con khi predator bậc 2 không tồn tại hoặc không xâm nhập được.

Ý nghĩa sinh học: khi predator bậc 2 bị loại bỏ, hệ ba thành phần nutrient-prey-predator 1 vẫn có thể ổn định về một trạng thái cân bằng bền vững.

## Kết luận cho notebook 02

Các hình trong notebook 02 bổ sung cho notebook 01 bằng cách tập trung vào ổn định toàn cục và persistence:

- Hàm Lyapunov giảm dọc nghiệm cho thấy cơ chế ổn định của `P1` và `P2`.
- Nhiều điều kiện đầu dương vẫn duy trì `x,y,z` cách xa 0, minh họa uniform persistence.
- Cân bằng nội `P3` thể hiện trạng thái coexistence của toàn bộ chuỗi thức ăn.

Về mặt mô hình hóa, notebook này cho thấy paper không chỉ phân tích ổn định cục bộ bằng trị riêng, mà còn dùng Lyapunov và persistence để kết luận hành vi dài hạn của hệ.

## Bản giải thích chi tiết để đưa vào báo cáo

Notebook 02 chuyển từ phân tích cục bộ sang phân tích dài hạn. Nếu notebook 01 trả lời câu hỏi "hệ tiến về cân bằng biên nào?", thì notebook 02 trả lời câu hỏi quan trọng hơn: "khi nào toàn bộ chuỗi thức ăn có thể tồn tại lâu dài?".

### 1. Ý nghĩa của coexistence equilibrium P3

Cân bằng nội:

```text
P3 = (S3, x3, y3, z3)
```

là trạng thái trong đó nutrient, prey, predator bậc 1 và predator bậc 2 đều có giá trị dương. Đây là trạng thái sinh học mong muốn nếu mục tiêu là duy trì toàn bộ chuỗi thức ăn trong chemostat.

Trong hình time series, nếu cả `x,y,z` đều không tiến về 0 thì ta có bằng chứng số cho coexistence. Nếu quỹ đạo hội tụ về `P3`, coexistence là trạng thái tĩnh. Nếu quỹ đạo dao động quanh `P3`, coexistence vẫn xảy ra nhưng dưới dạng dao động.

### 2. Vì sao cần chạy nhiều điều kiện đầu?

Một mô phỏng đơn lẻ chỉ cho thấy hệ tồn tại lâu dài với một trạng thái ban đầu cụ thể. Nhưng Theorem 3.4 nói mạnh hơn: hệ có tính uniform persistence trong miền dương. Điều này có nghĩa là với nhiều điều kiện đầu dương khác nhau, nghiệm không tiến sát biên tuyệt chủng.

Vì vậy notebook chạy nhiều điều kiện đầu và vẽ:

```text
min{x(t), y(t), z(t)}
```

Nếu đường này sau transient nằm cách 0, thì cả ba quần thể sinh vật đều được duy trì. Đây là cách trực quan để biểu diễn persistence: không chỉ một loài sống sót, mà loài yếu nhất tại mỗi thời điểm cũng không bị kéo về 0.

### 3. Liên hệ persistence với các cân bằng biên

Trong paper, persistence được chứng minh bằng cách xét các cân bằng trên biên như `P1` và `P2`. Nếu các cân bằng biên đẩy nghiệm nội ra khỏi biên theo hướng loài bị thiếu, thì nghiệm trong miền dương không thể hội tụ về biên.

Diễn giải sinh học:

```text
Nếu predator 1 có thể xâm nhập trạng thái prey-only,
và predator 2 có thể xâm nhập trạng thái prey-predator1,
thì toàn bộ chuỗi thức ăn có khả năng cùng tồn tại.
```

Đây là lý do Theorem 3.4 liên hệ chặt với các điều kiện ổn định/mất ổn định của `P1` và `P2`.

### 4. Vai trò của hàm Lyapunov V tại P1

Hàm:

```text
V(S,x) = 1/2 (S-S1)^2 + 1/2 (x-x1)^2
```

đo khoảng cách của nghiệm trong hệ con `(S,x)` đến cân bằng `P1`. Khi `V(t)` giảm dần, ta hiểu rằng nghiệm đang mất "năng lượng sai lệch" và tiến gần hơn đến cân bằng.

Nếu chỉ dùng trị riêng, ta chỉ biết ổn định gần điểm cân bằng. Nhưng hàm Lyapunov giúp chứng minh ổn định trên một miền rộng hơn. Vì vậy hình `V(t)` giảm là minh họa rất tốt cho phương pháp chứng minh của paper.

### 5. Vai trò của hàm Lyapunov W tại P2

Hàm:

```text
W(S,x,y) = S - S2 - S2 ln(S/S2)
           + 1/2 (x-x2)^2
           + 1/2 (y-y2)^2
```

có hai phần:

- phần entropy-like cho nutrient `S`;
- phần bình phương cho `x` và `y`.

Phần `S - S2 - S2 ln(S/S2)` luôn không âm với `S>0` và bằng 0 khi `S=S2`. Nó phù hợp hơn bình phương đơn giản trong hệ dương vì giữ được cấu trúc sinh học của biến nutrient.

Khi `W(t)` giảm, ta có minh họa rằng hệ con `(S,x,y)` tiến về `P2`. Điều này tương ứng với Theorem 3.2.

### 6. Nhận xét tổng quát

Notebook 02 cho thấy paper có hai tầng lập luận:

```text
Tầng 1: phân tích cục bộ bằng Jacobian và Routh-Hurwitz.
Tầng 2: phân tích toàn cục bằng Lyapunov và persistence.
```

Các hình Lyapunov giúp giải thích tầng 2. Các hình persistence giúp chuyển từ ổn định của hệ con sang kết luận về coexistence của hệ đầy đủ.
