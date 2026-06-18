# Nhận xét notebook 01 - Basic properties and boundary equilibria

Notebook này tái hiện các kết quả cơ bản ở Section 2 của paper: tính không âm, tính bị chặn, tính tiêu tán và các cân bằng biên `P0`, `P1`, `P2`.

## Experiment 1 - Positivity, boundedness, dissipativity

Hình time series của `S(t), x(t), y(t), z(t)` cho thấy các nghiệm xuất phát từ điều kiện đầu dương luôn nằm trong miền không âm. Không có biến nào đi xuống giá trị âm trong suốt quá trình mô phỏng, phù hợp với ý nghĩa sinh học của mô hình chemostat.

Đồ thị tổng `S(t)+x(t)+y(t)+z(t)` cho thấy tổng nồng độ không tăng vô hạn mà sau một khoảng thời gian ban đầu sẽ nằm trong một miền bị chặn. Đây là minh họa số cho Theorem 2.1: hệ là dissipative và nghiệm cuối cùng bị hút vào một miền compact.

Ý nghĩa sinh học: hệ chemostat không tạo ra tăng trưởng vô hạn. Dòng vào, rửa trôi và tương tác tiêu thụ làm cho toàn bộ hệ bị khống chế trong một khoảng hữu hạn.

## Experiment 2 - Washout equilibrium P0

Trong thí nghiệm này ta chọn tham số sao cho:

```text
f1(1) < D1
```

Nghĩa là ngay cả khi nồng độ dinh dưỡng đạt mức lớn nhất `S=1`, tốc độ tăng trưởng của con mồi vẫn nhỏ hơn tốc độ loại bỏ. Vì vậy con mồi `x` không thể tồn tại lâu dài.

Hình time series cho thấy:

```text
S(t) -> 1
x(t) -> 0
y(t) -> 0
z(t) -> 0
```

Kết quả này phù hợp với Theorem 2.2. Điểm cân bằng washout `P0=(1,0,0,0)` là ổn định tiệm cận cục bộ khi `f1(1)-D1<0`.

Ý nghĩa sinh học: nếu tốc độ loại bỏ của con mồi quá lớn hoặc khả năng sử dụng dinh dưỡng quá yếu, toàn bộ chuỗi thức ăn bị rửa trôi khỏi chemostat, chỉ còn lại dinh dưỡng.

## Experiment 3 - Boundary equilibrium P1

Trong thí nghiệm `P1`, con mồi có thể tồn tại nhờ dinh dưỡng, nhưng predator bậc 1 không thể xâm nhập. Điều kiện được kiểm tra trong notebook là:

```text
f2(x1) - D2 < 0
```

với:

```text
P1 = (S1, x1, 0, 0)
```

Hình time series cho thấy `S(t)` và `x(t)` hội tụ về các giá trị dương, trong khi `y(t)` và `z(t)` tiến về 0. Điều này khớp với diễn giải của điểm cân bằng biên `P1`: nutrient và prey cùng tồn tại, còn hai predator bị tuyệt chủng.

Hình phase portrait trong mặt phẳng `(S,x)` cho thấy quỹ đạo tiến dần về điểm đỏ `P1`. Đây là minh họa trực quan cho tính ổn định của `P1` trong hệ con `(S,x)`, tương ứng với Theorem 2.4 và phần ổn định toàn cục ở Theorem 3.1.

Ý nghĩa sinh học: prey đủ khả năng khai thác nutrient để sống sót, nhưng mật độ prey cân bằng không đủ để predator bậc 1 duy trì quần thể.

## Experiment 4 - Boundary equilibrium P2

Trong thí nghiệm `P2`, nutrient, prey và predator bậc 1 cùng tồn tại, nhưng predator bậc 2 bị loại bỏ. Điều kiện xâm nhập của predator bậc 2 được kiểm tra là:

```text
f3(y2) - D3 < 0
```

với:

```text
P2 = (S2, x2, y2, 0)
```

Hình time series cho thấy:

```text
S(t) -> S2 > 0
x(t) -> x2 > 0
y(t) -> y2 > 0
z(t) -> 0
```

Điều này phù hợp với Theorem 2.8: `P2` ổn định khi predator bậc 2 không thể xâm nhập.

Hình quỹ đạo 3D trong không gian `(S,x,y)` tiến về điểm đỏ `P2`, cho thấy hệ con gồm nutrient, prey và predator bậc 1 có cấu trúc ổn định. Thành phần `z` bị triệt tiêu nên không xuất hiện trong không gian pha này.

Ý nghĩa sinh học: predator bậc 1 có đủ nguồn thức ăn để tồn tại, nhưng predator bậc 2 không đủ lợi thế tăng trưởng so với tốc độ loại bỏ.

## Kết luận cho notebook 01

Các hình trong notebook 01 tái hiện chuỗi kết quả nền tảng của paper:

- Nếu prey không xâm nhập được, hệ tiến về `P0`.
- Nếu prey sống được nhưng predator 1 không xâm nhập được, hệ tiến về `P1`.
- Nếu predator 1 sống được nhưng predator 2 không xâm nhập được, hệ tiến về `P2`.
- Trong mọi trường hợp, nghiệm dương vẫn không âm và bị chặn.

Các mô phỏng này làm rõ vai trò của điều kiện xâm nhập `fi(equilibrium)-Di`: một loài chỉ tồn tại lâu dài nếu tốc độ tăng trưởng tại trạng thái biên lớn hơn tốc độ loại bỏ của nó.

## Bản giải thích chi tiết để đưa vào báo cáo

Notebook 01 nên được hiểu như phần kiểm chứng số cho toàn bộ Section 2 của bài báo. Trong Section 2, tác giả chưa đi vào phân nhánh hay persistence sâu, mà trước hết chứng minh rằng mô hình có ý nghĩa toán học và sinh học: nghiệm tồn tại trong miền không âm, bị chặn, và các điểm cân bằng biên có thể ổn định hoặc mất ổn định tùy điều kiện tham số.

### 1. Vì sao cần kiểm tra nghiệm không âm?

Trong mô hình, `S, x, y, z` lần lượt là nồng độ dinh dưỡng, con mồi, predator bậc 1 và predator bậc 2. Các đại lượng này không thể âm trong thực tế. Vì vậy nếu nghiệm số đi xuống âm, mô hình hoặc thuật toán mô phỏng sẽ mất ý nghĩa sinh học.

Hình time series ở thí nghiệm đầu cho thấy tất cả biến đều giữ giá trị không âm. Đây là kiểm chứng trực quan cho tính bất biến dương của miền `R_+^4`. Nói cách khác, nếu ban đầu hệ có nồng độ dương thì động lực học của hệ không đẩy nghiệm ra khỏi miền sinh học hợp lệ.

### 2. Vì sao cần kiểm tra bị chặn và dissipativity?

Nếu mô hình cho phép `S+x+y+z` tăng vô hạn, hệ sẽ không phù hợp với chemostat vì chemostat có dòng vào, dòng ra và tài nguyên hữu hạn. Theorem 2.1 của paper chứng minh rằng nghiệm cuối cùng đi vào một miền bị chặn.

Đồ thị tổng `S+x+y+z` trong notebook minh họa điều này. Ban đầu tổng có thể thay đổi do điều kiện đầu và do tương tác giữa các loài, nhưng về lâu dài nó không tăng vô hạn. Điều này cho phép các phân tích sau như ổn định, persistence và bifurcation có cơ sở, vì quỹ đạo được giữ trong một miền hữu hạn.

### 3. Cách đọc thí nghiệm P0

Điểm `P0=(1,0,0,0)` là trạng thái washout: nutrient đạt mức vào chuẩn hóa là 1, còn tất cả sinh vật bị loại bỏ.

Điều kiện quan trọng là:

```text
f1(1) < D1
```

Tại `S=1`, đây là môi trường thuận lợi nhất cho prey vì nutrient lớn nhất. Nếu ngay cả khi đó prey vẫn có tốc độ tăng trưởng nhỏ hơn tốc độ loại bỏ, thì prey không thể tồn tại. Khi prey mất đi, predator bậc 1 và bậc 2 cũng mất nguồn thức ăn và bị rửa trôi.

Vì vậy hình hội tụ về `S=1`, `x=y=z=0` không chỉ là kết quả số, mà phản ánh đúng chuỗi nhân quả sinh học: prey không xâm nhập được dẫn đến toàn bộ food chain sụp đổ.

### 4. Cách đọc thí nghiệm P1

Điểm `P1=(S1,x1,0,0)` biểu diễn trạng thái prey-only. Ở đây prey và nutrient cùng tồn tại, nhưng predator bậc 1 và bậc 2 biến mất.

Điều kiện then chốt là predator bậc 1 không xâm nhập được:

```text
f2(x1) < D2
```

Trong đó `x1` là mật độ prey tại cân bằng prey-only. Nếu `x1` quá thấp, predator bậc 1 không đủ nguồn thức ăn để bù cho tốc độ loại bỏ `D2`.

Hình time series cho thấy `S` và `x` tiến về giá trị dương, còn `y,z` tiến về 0. Hình phase portrait `(S,x)` cho thấy quỹ đạo bị hút về điểm `P1`. Đây là minh họa cho tính ổn định của hệ con nutrient-prey.

### 5. Cách đọc thí nghiệm P2

Điểm `P2=(S2,x2,y2,0)` biểu diễn trạng thái nutrient, prey và predator bậc 1 cùng tồn tại, nhưng predator bậc 2 tuyệt chủng.

Điều kiện quan trọng là:

```text
f3(y2) < D3
```

Tức là tại mật độ predator bậc 1 cân bằng `y2`, predator bậc 2 không tăng trưởng đủ nhanh để tồn tại. Khi đó `z(t)` tiến về 0, trong khi `S,x,y` tiến về các giá trị dương.

Hình 3D trong không gian `(S,x,y)` giúp thấy rõ rằng sau khi bỏ qua thành phần `z`, hệ ba biến còn lại tiến về một điểm cân bằng. Điều này khớp với Theorem 2.8: `P2` ổn định khi predator bậc 2 không thể xâm nhập.

### 6. Nhận xét tổng quát

Ba cân bằng `P0`, `P1`, `P2` tạo thành một chuỗi kịch bản sinh thái:

```text
P0: không loài nào sống được
P1: chỉ prey sống được
P2: prey và predator 1 sống được
```

Sự khác nhau giữa các kịch bản nằm ở khả năng xâm nhập của loài tiếp theo trong chuỗi thức ăn. Đây là ý tưởng trung tâm của mô hình: một loài có thể tồn tại nếu tốc độ tăng trưởng tại trạng thái hiện tại lớn hơn tốc độ loại bỏ của nó.
