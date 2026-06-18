# Nhận xét notebook 03 - Hopf bifurcation

Notebook này tái hiện phần Section 4 của paper về Hopf bifurcation. Tham số phân nhánh được chọn là `lambda` trong hàm đáp ứng:

```text
f1(S, lambda) = lambda S / (b1 + S)
```

Khi `lambda` thay đổi, tốc độ tăng trưởng cực đại của prey trên nutrient thay đổi. Điều này có thể làm cân bằng mất ổn định và sinh ra nghiệm tuần hoàn.

## Experiment 1 - Eigenvalue crossing near P2

Hình đầu tiên vẽ phần thực lớn nhất của các trị riêng Jacobian quanh cân bằng biên:

```text
P2 = (S2, x2, y2, 0)
```

Khi đường `max Re(eigenvalue)` cắt trục 0, cân bằng chuyển từ ổn định sang không ổn định hoặc ngược lại. Đây là dấu hiệu quan trọng của Hopf bifurcation nếu cặp trị riêng liên quan là cặp phức liên hợp.

Hình thứ hai vẽ độ lớn phần ảo của trị riêng chi phối. Phần ảo khác 0 cho thấy trị riêng vượt trục ảo dưới dạng cặp phức liên hợp, không phải trị riêng thực đơn. Điều này phù hợp với điều kiện Hopf trong Theorem 4.2.

Diễn giải toán học:

```text
Re(lambda_eig) = 0
Im(lambda_eig) != 0
```

tại giá trị phân nhánh. Khi điều kiện xuyên trục được thỏa mãn, nghiệm tuần hoàn có thể xuất hiện từ cân bằng.

Ý nghĩa sinh học: khi khả năng khai thác nutrient của prey thay đổi, trạng thái ổn định nutrient-prey-predator 1 có thể mất ổn định và chuyển sang dao động chu kỳ.

## Experiment 2 - Time series before and after the crossing

Notebook so sánh nghiệm tại hai giá trị `lambda` đại diện.

Ở giá trị `lambda` nằm trong vùng ổn định, time series có xu hướng tiến về trạng thái cân bằng. Biên độ dao động giảm dần sau giai đoạn quá độ. Điều này tương ứng với trường hợp các trị riêng có phần thực âm.

Ở giá trị `lambda` sau khi vượt qua vùng đổi ổn định, time series biểu hiện dao động kéo dài. Các biến không hội tụ đơn điệu về một điểm mà duy trì dao động có chu kỳ hoặc gần chu kỳ. Đây là dấu hiệu trực quan của nghiệm tuần hoàn phát sinh sau Hopf bifurcation.

Hình phase portrait dài hạn trong mặt phẳng `(x,y)` cho thấy:

- Nếu cân bằng ổn định: quỹ đạo co lại gần một điểm.
- Nếu xuất hiện dao động: quỹ đạo tạo thành vòng kín hoặc vùng dao động lặp lại.

Kết quả này minh họa kết luận của Theorem 4.2: Hopf bifurcation dẫn đến một họ nghiệm tuần hoàn phân nhánh từ `P2`.

## Experiment 3 - Numerical bifurcation diagram

Hình bifurcation diagram vẽ cực đại và cực tiểu dài hạn của `x(t)` theo tham số `lambda`:

```text
lambda -> max x(t), min x(t)
```

sau khi đã bỏ qua giai đoạn transient.

Nếu nghiệm hội tụ về cân bằng, max và min gần như trùng nhau. Khi xuất hiện dao động chu kỳ, max và min tách ra thành hai nhánh khác nhau. Khoảng cách giữa hai nhánh biểu diễn biên độ dao động.

Vì vậy, vùng hai nhánh tách biệt trong hình chính là bằng chứng số cho sự xuất hiện dao động sau Hopf bifurcation.

Ý nghĩa sinh học: khi tham số tăng trưởng của prey thay đổi, mật độ prey không còn ổn định ở một giá trị cố định mà dao động giữa giá trị thấp và cao. Sự dao động này kéo theo dao động của predator và nutrient.

## Liên hệ với Theorem 4.3

Paper cũng chứng minh Hopf bifurcation tại cân bằng nội:

```text
P3 = (S3, x3, y3, z3)
```

Notebook này trình bày đầy đủ quy trình số cho `P2` vì trường hợp `P2` dễ cô lập ngưỡng phân nhánh hơn. Với `P3`, quy trình tương tự:

1. Giải cân bằng `P3(lambda)`.
2. Tính Jacobian 4x4 tại `P3(lambda)`.
3. Theo dõi cặp trị riêng phức cắt trục ảo.
4. Mô phỏng ODE trước và sau ngưỡng.
5. Vẽ bifurcation diagram bằng long-run max/min.

Do đó, notebook này tái hiện phương pháp phân tích của Section 4 và minh họa rõ nhất cơ chế Hopf bằng mô phỏng.

## Kết luận cho notebook 03

Các hình trong notebook 03 cho thấy:

- Trị riêng của Jacobian thay đổi theo tham số `lambda`.
- Một cặp trị riêng phức có thể cắt trục ảo.
- Sau ngưỡng phân nhánh, nghiệm có thể chuyển từ hội tụ cân bằng sang dao động tuần hoàn.
- Bifurcation diagram thể hiện sự tách nhánh max/min, tương ứng với biên độ dao động khác 0.

Về mặt mô hình hóa, đây là phần giải thích tại sao hệ chemostat không chỉ có các trạng thái ổn định hoặc tuyệt chủng, mà còn có thể xuất hiện các dao động population cycle khi tham số sinh học thay đổi.

## Bản giải thích chi tiết để đưa vào báo cáo

Notebook 03 minh họa phân nhánh Hopf tại cân bằng biên `P2`. Đây là trường hợp predator bậc 2 bị rửa trôi, nhưng hệ nutrient-prey-predator1 vẫn có thể chuyển từ cân bằng ổn định sang dao động.

### 1. Vì sao chọn lambda trong f1?

Ta chọn:

```text
f1(S, lambda) = lambda S / (b1 + S)
```

Tham số `lambda` là tốc độ tăng trưởng cực đại của prey khi khai thác nutrient. Khi `lambda` tăng, prey có thể phản ứng mạnh hơn với nutrient. Điều này làm thay đổi cân bằng năng lượng giữa nutrient, prey và predator bậc 1.

Trong ngôn ngữ mô hình hóa, `lambda` là tham số điều khiển. Bằng cách quét `lambda`, ta kiểm tra độ nhạy và độ bền của cấu trúc ổn định.

### 2. Cách đọc hình trị riêng

Jacobian tại `P2` mô tả động học tuyến tính gần cân bằng. Nếu mọi trị riêng có phần thực âm, nhiễu nhỏ quanh `P2` sẽ suy giảm và `P2` ổn định cục bộ.

Nếu phần thực lớn nhất của trị riêng vượt qua 0, nhiễu nhỏ không còn suy giảm. Với Hopf bifurcation, điều kiện đặc biệt là cặp trị riêng phức liên hợp cắt trục ảo:

```text
alpha(lambda) ± i beta(lambda)
```

tại đó:

```text
alpha(lambda*) = 0
beta(lambda*) != 0
```

Hình `max Re(eigenvalue)` cho biết thời điểm mất ổn định. Hình `|Im(eigenvalue)|` xác nhận rằng trị riêng có phần ảo khác 0, tức là dạng mất ổn định mang tính dao động.

### 3. Cách đọc time series trước/sau Hopf

Trước Hopf, nghiệm có thể dao động ban đầu do điều kiện đầu không nằm đúng tại cân bằng, nhưng biên độ giảm dần. Điều này phản ánh phần thực trị riêng âm.

Sau Hopf, dao động không tắt. Nghiệm đi vào một chu kỳ giới hạn hoặc dao động lâu dài quanh cân bằng. Điều này phản ánh việc cân bằng đã mất ổn định và một nghiệm tuần hoàn xuất hiện.

Về sinh học, điều này có nghĩa là hệ không còn duy trì mật độ prey và predator cố định. Thay vào đó, prey tăng lên, predator phản ứng tăng sau đó, prey giảm, predator giảm, rồi chu kỳ lặp lại.

### 4. Cách đọc phase portrait

Trong mặt phẳng `(x,y)`:

- nếu quỹ đạo xoắn vào một điểm, hệ hội tụ về cân bằng;
- nếu quỹ đạo tạo vòng lặp, hệ có dao động tuần hoàn.

Phase portrait giúp nhìn cấu trúc động học rõ hơn time series. Time series cho thấy dao động theo thời gian, còn phase portrait cho thấy quan hệ trễ pha giữa prey và predator.

### 5. Cách đọc bifurcation diagram

Bifurcation diagram vẽ:

```text
lambda -> max x(t), min x(t)
```

sau khi bỏ qua transient.

Nếu nghiệm hội tụ về cân bằng, `max x(t)` và `min x(t)` gần như bằng nhau, nên hai nhánh chồng lên nhau. Nếu nghiệm dao động, `max` và `min` tách nhau, tạo thành vùng biên độ khác 0.

Do đó, hình bifurcation diagram là bằng chứng số gọn nhất cho sự xuất hiện nghiệm tuần hoàn khi tham số thay đổi.

### 6. Nhận xét tổng quát

Notebook 03 bổ sung cho report mẫu ở điểm quan trọng: report chỉ nêu điều kiện Hopf bằng lời, còn notebook trực tiếp vẽ:

```text
trị riêng -> time series -> phase portrait -> bifurcation diagram
```

Chuỗi hình này cho thấy rõ cơ chế từ mất ổn định tuyến tính đến dao động phi tuyến dài hạn.
