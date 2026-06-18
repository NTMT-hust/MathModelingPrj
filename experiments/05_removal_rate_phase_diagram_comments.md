# Nhận xét notebook 05 - Removal-rate phase diagram

Notebook 05 bổ sung một thí nghiệm số tập trung trực tiếp vào điểm mô hình hóa quan trọng của paper: các tốc độ loại bỏ `D1`, `D2`, `D3` là khác nhau. Khi các removal rates khác nhau, luật bảo toàn trong các mô hình chemostat đơn giản không còn đúng, nên cần nghiên cứu hệ đầy đủ bốn chiều gồm `S, x, y, z`.

Thí nghiệm này cố định `D1` và quét hai tham số:

```text
D2: tốc độ loại bỏ của predator bậc 1 y
D3: tốc độ loại bỏ của predator bậc 2 z
```

Mục tiêu là vẽ phase diagram trong mặt phẳng `(D2, D3)` để xem hệ chuyển giữa các trạng thái dài hạn nào khi hai tốc độ loại bỏ này thay đổi.

## 1. Mục tiêu của thí nghiệm

Các notebook trước đã minh họa từng loại cân bằng riêng lẻ:

```text
P0: washout
P1: prey-only
P2: nutrient-prey-predator1 coexistence, z extinct
P3: full coexistence
Hopf-like oscillation
```

Notebook 05 đi thêm một bước: thay vì chọn từng bộ tham số riêng, ta quét cả một miền tham số `(D2, D3)` và phân loại kết quả dài hạn tại từng điểm.

Vì vậy heatmap trả lời câu hỏi:

```text
Nếu predator 1 và predator 2 có tốc độ loại bỏ khác nhau,
hệ chemostat sẽ đi về trạng thái sinh thái nào?
```

Đây là thí nghiệm rất phù hợp với paper vì paper nhấn mạnh rằng distinct removal rates làm hệ không thể rút gọn đơn giản và có thể tạo ra nhiều hành vi động học khác nhau.

## 2. Mô hình được sử dụng

Notebook dùng hệ ODE:

```text
dS/dt = 1 - S - f1(S)x
dx/dt = x(f1(S)-D1) - f2(x)y
dy/dt = y(f2(x)-D2) - f3(y)z
dz/dt = z(f3(y)-D3)
```

Trong đó:

```text
S: nutrient
x: prey
y: predator bậc 1
z: predator bậc 2
```

Các hàm đáp ứng là Monod:

```text
f1(S) = a1 S / (K1 + S)
f2(x) = a2 x / (K2 + x)
f3(y) = a3 y / (K3 + y)
```

Dạng Monod thỏa các giả thiết của paper:

```text
fi(0) = 0
fi'(u) > 0 với u > 0
```

## 3. Cách thực hiện thí nghiệm

Notebook cố định `D1`, sau đó tạo lưới giá trị:

```text
D2_values = nhiều giá trị trong khoảng [0.15, 2.30]
D3_values = nhiều giá trị trong khoảng [0.08, 1.20]
```

Với mỗi cặp `(D2, D3)`, notebook:

1. giải hệ ODE bằng `scipy.integrate.solve_ivp`;
2. bỏ qua phần transient ban đầu;
3. tính trung bình dài hạn của `S, x, y, z`;
4. tính biên độ dao động dài hạn;
5. phân loại chế độ dài hạn của hệ.

Mặc định notebook dùng lưới `50 x 50`, tức là 2500 lần mô phỏng. Đây là mức đủ mịn để thấy cấu trúc heatmap nhưng vẫn chạy được trên laptop thông thường.

## 4. Quy tắc phân loại regime

Notebook phân loại mỗi điểm tham số thành một trong năm lớp:

```text
0: Washout
1: Prey only
2: P2 boundary
3: Stable P3
4: Oscillatory coexistence
```

Ý nghĩa từng lớp:

### Class 0 - Washout

Điều kiện:

```text
x, y, z đều gần 0
```

Trạng thái tương ứng:

```text
P0 = (1, 0, 0, 0)
```

Ý nghĩa sinh học: không loài sinh vật nào sống sót, chỉ còn nutrient trong chemostat.

### Class 1 - Prey only

Điều kiện:

```text
x > 0
y ≈ 0
z ≈ 0
```

Trạng thái tương ứng:

```text
P1 = (S1, x1, 0, 0)
```

Ý nghĩa sinh học: prey sống được nhờ nutrient, nhưng predator bậc 1 bị loại bỏ. Khi predator bậc 1 biến mất, predator bậc 2 cũng không có nguồn thức ăn.

### Class 2 - P2 boundary

Điều kiện:

```text
x > 0
y > 0
z ≈ 0
```

Trạng thái tương ứng:

```text
P2 = (S2, x2, y2, 0)
```

Ý nghĩa sinh học: nutrient, prey và predator bậc 1 cùng tồn tại, nhưng predator bậc 2 không thể duy trì quần thể.

### Class 3 - Stable P3

Điều kiện:

```text
x > 0, y > 0, z > 0
biên độ dao động dài hạn nhỏ
```

Trạng thái tương ứng:

```text
P3 = (S3, x3, y3, z3)
```

Ý nghĩa sinh học: toàn bộ chuỗi thức ăn cùng tồn tại và tiến về một cân bằng ổn định.

### Class 4 - Oscillatory coexistence

Điều kiện:

```text
x > 0, y > 0, z > 0
biên độ dao động dài hạn lớn
```

Ý nghĩa sinh học: toàn bộ chuỗi thức ăn cùng tồn tại nhưng không hội tụ về một điểm cân bằng. Thay vào đó, các quần thể dao động lâu dài, giống hành vi Hopf-like.

## 5. Cách đọc heatmap

Heatmap có:

```text
trục ngang: D2
trục dọc: D3
màu sắc: regime dài hạn
```

Mỗi pixel trong heatmap là kết quả của một mô phỏng ODE tại một cặp `(D2, D3)`.

Cách diễn giải:

- Khi `D2` tăng, predator bậc 1 bị loại bỏ mạnh hơn. Do đó vùng prey-only thường mở rộng vì `y` khó tồn tại.
- Khi `D3` tăng, predator bậc 2 bị loại bỏ mạnh hơn. Do đó hệ dễ rơi về trạng thái `P2`, nơi `z=0`.
- Khi cả `D2` và `D3` đủ thấp, predator có cơ hội tồn tại, nên có thể xuất hiện coexistence hoặc dao động.
- Vùng stable `P3` cho thấy cả bốn thành phần cùng tồn tại ổn định.
- Vùng oscillatory coexistence cho thấy coexistence không ổn định tĩnh mà chuyển thành dao động.

Heatmap vì vậy cho thấy các removal rates không chỉ thay đổi giá trị cân bằng, mà còn có thể thay đổi loại hành vi dài hạn của toàn hệ.

## 6. Cách đọc các time series đại diện

Notebook tự chọn một số điểm đại diện trên heatmap và vẽ time series.

### Prey-only case

Hình prey-only cho thấy:

```text
x(t) duy trì giá trị dương
y(t), z(t) tiến về 0
```

Điều này xảy ra khi `D2` đủ lớn khiến predator bậc 1 không thể tồn tại. Vì `z` ăn `y`, nên `z` cũng biến mất.

### P2 boundary case

Hình P2 cho thấy:

```text
S(t), x(t), y(t) duy trì giá trị dương
z(t) tiến về 0
```

Đây là trường hợp predator bậc 1 sống được, nhưng predator bậc 2 bị loại bỏ do `D3` lớn hoặc do nguồn thức ăn `y` không đủ.

### Stable P3 case

Hình stable P3 cho thấy:

```text
S(t), x(t), y(t), z(t) đều dương
dao động nhỏ và suy giảm
```

Hệ tiến về cân bằng nội. Đây là trạng thái coexistence ổn định.

### Oscillatory coexistence case

Hình oscillatory coexistence cho thấy:

```text
S(t), x(t), y(t), z(t) đều dương
dao động không tắt sau transient
```

Đây là dấu hiệu của hành vi Hopf-like. Tất cả loài tồn tại, nhưng mật độ thay đổi theo chu kỳ.

## 7. Ý nghĩa sinh học của D2 và D3

`D2` và `D3` có thể được hiểu là tổng hợp của rửa trôi và tử vong riêng:

```text
D2 = washout + death rate của predator 1
D3 = washout + death rate của predator 2
```

Khi `D2` lớn, predator bậc 1 cần nhiều prey hơn để bù lại mất mát. Nếu prey không đủ, `y` tuyệt chủng.

Khi `D3` lớn, predator bậc 2 cần nhiều predator bậc 1 hơn để tồn tại. Nếu `y` không đủ, `z` tuyệt chủng.

Do đó thay đổi `D2` và `D3` làm thay đổi khả năng xâm nhập của từng tầng trong chuỗi thức ăn. Đây chính là cơ chế tạo ra các vùng khác nhau trong heatmap.

## 8. Liên hệ với paper

Paper nhấn mạnh rằng khi các removal rates khác nhau, luật bảo toàn không còn đúng. Vì vậy không thể đơn giản giảm hệ xuống số chiều thấp hơn như trong một số mô hình chemostat cổ điển.

Notebook 05 minh họa điểm này bằng số:

```text
chỉ cần thay đổi D2 và D3,
hệ có thể chuyển giữa P0, P1, P2, P3 và dao động Hopf-like.
```

Điều này chứng minh rằng distinct removal rates không phải chi tiết kỹ thuật nhỏ. Chúng ảnh hưởng trực tiếp đến cấu trúc động học của mô hình.

## 9. Các hình và file được tạo

Notebook lưu các hình vào:

```text
figures/removal_rate_phase_diagram/
```

Các file chính:

```text
removal_rate_phase_diagram_heatmap.png
timeseries_1_prey_only.png
timeseries_2_p2_boundary.png
timeseries_3_stable_p3.png
timeseries_4_oscillatory_coexistence.png
representative_regime_summary.csv
```

Heatmap là hình chính nên đưa vào báo cáo. Các time series có thể dùng để giải thích từng vùng màu trong heatmap.

## 10. Đoạn nhận xét có thể đưa vào báo cáo

Phiên bản tiếng Việt:

```text
Để khảo sát ảnh hưởng của các tốc độ loại bỏ khác nhau, chúng tôi cố định D1 và quét D2, D3 trên một lưới tham số. Với mỗi cặp (D2,D3), hệ ODE được giải số, phần transient ban đầu được loại bỏ, sau đó nghiệm dài hạn được phân loại thành washout, prey-only, P2 boundary, stable P3 hoặc oscillatory coexistence. Heatmap thu được cho thấy các removal rates có ảnh hưởng quyết định đến trạng thái sinh thái cuối cùng. Khi D2 lớn, predator bậc 1 khó tồn tại và hệ thường rơi về trạng thái prey-only. Khi D3 lớn, predator bậc 2 bị loại bỏ và hệ chuyển về cân bằng biên P2. Với một số miền tham số, cả ba quần thể sinh vật cùng tồn tại ổn định hoặc dao động lâu dài. Kết quả này minh họa rõ nhận định của paper rằng các removal rates khác nhau làm mất luật bảo toàn và khiến động học đầy đủ bốn chiều trở nên cần thiết.
```

Phiên bản tiếng Anh:

```text
To investigate the effect of distinct removal rates, we fixed D1 and swept D2 and D3 over a two-dimensional parameter grid. For each pair (D2,D3), the ODE system was solved numerically, the transient part was discarded, and the long-term solution was classified as washout, prey-only, P2 boundary coexistence, stable P3 coexistence, or oscillatory coexistence. The resulting heatmap shows that removal rates strongly determine the final ecological regime. Large D2 makes the first predator difficult to sustain and often leads to the prey-only state, whereas large D3 removes the top predator and pushes the system toward the P2 boundary equilibrium. In other regions, all species coexist either at a stable equilibrium or through sustained oscillations. This numerical experiment supports the paper's key modelling point that distinct removal rates destroy the conservation-law reduction and make the full four-dimensional dynamics essential.
```

## 11. Kết luận cho notebook 05

Notebook 05 là một thí nghiệm tổng hợp. Nó không chỉ tái hiện một theorem riêng lẻ, mà trực quan hóa vai trò của removal rates trong toàn bộ mô hình.

Thông điệp chính:

```text
Distinct removal rates can change the ecological outcome.
They can move the system from extinction to boundary survival,
from boundary survival to full coexistence,
and from stable coexistence to oscillatory coexistence.
```

Vì vậy heatmap `(D2,D3)` là một hình rất nên đưa vào báo cáo cuối cùng.
