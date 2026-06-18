# Nhận xét notebook 04 - Hopf bifurcation tại P3

Notebook này bổ sung phần còn thiếu so với report mẫu: minh họa Hopf bifurcation tại cân bằng nội `P3`, tương ứng với Section 4.3 và Theorem 4.3 của paper.

## Experiment 1 - Positive equilibrium P3 exists

Notebook trước hết kiểm tra cân bằng:

```text
P3 = (S3, x3, y3, z3)
```

với nhiều giá trị `lambda` quanh vùng phân nhánh. Các giá trị in ra đều dương, tức là cân bằng đang xét nằm trong miền nội của hệ:

```text
S3 > 0, x3 > 0, y3 > 0, z3 > 0
```

Điều này quan trọng vì Theorem 4.3 nói về Hopf bifurcation tại cân bằng coexistence, không phải cân bằng biên. Nếu một thành phần bằng 0, ta sẽ quay lại trường hợp `P1` hoặc `P2`.

## Experiment 2 - Eigenvalue crossing at P3

Hình đầu tiên vẽ phần thực lớn nhất của trị riêng Jacobian 4x4 tại `P3(lambda)`.

Khi đường này cắt trục 0, cân bằng `P3` đổi tính ổn định. Trước điểm cắt, phần thực lớn nhất âm nên nhiễu nhỏ quanh `P3` suy giảm. Sau điểm cắt, phần thực lớn nhất dương nên nhiễu nhỏ được khuếch đại.

Hình thứ hai vẽ độ lớn phần ảo của trị riêng chi phối. Vì phần ảo khác 0 tại điểm cắt, trị riêng vượt trục ảo dưới dạng một cặp phức liên hợp. Đây là dấu hiệu đặc trưng của Hopf bifurcation:

```text
Re(lambda_eig) = 0
Im(lambda_eig) != 0
```

Kết quả này minh họa điều kiện chính trong Theorem 4.3: tại một giá trị tham số tới hạn, cặp trị riêng phức của Jacobian tại `P3` cắt trục ảo.

## Experiment 3 - Time series before and after Hopf at P3

Notebook so sánh hai giá trị `lambda`:

- Một giá trị trước ngưỡng Hopf.
- Một giá trị sau ngưỡng Hopf.

Trước ngưỡng, các đường `S(t), x(t), y(t), z(t)` có xu hướng quay về các mức cân bằng dương. Dao động ban đầu là do điều kiện đầu bị perturb khỏi `P3`, nhưng biên độ giảm dần theo thời gian.

Sau ngưỡng, các biến không hội tụ về hẳn một điểm. Thay vào đó, chúng duy trì dao động quanh cân bằng coexistence. Điều quan trọng là dao động vẫn nằm trong miền dương, tức là cả prey, predator bậc 1 và predator bậc 2 đều tiếp tục tồn tại.

Hình phase portrait 3D trong không gian `(x,y,z)` cho thấy sự khác biệt:

- Trước Hopf: quỹ đạo co về điểm `P3`.
- Sau Hopf: quỹ đạo tạo thành vòng dao động quanh `P3`.

Ý nghĩa sinh học: coexistence không nhất thiết là trạng thái tĩnh. Khi tham số tăng trưởng của prey thay đổi, toàn bộ chuỗi thức ăn có thể chuyển sang coexistence dao động.

## Experiment 4 - Numerical bifurcation diagram at P3

Hình bifurcation diagram vẽ cực đại và cực tiểu dài hạn của `x(t)` theo `lambda`:

```text
lambda -> max x(t), min x(t)
```

Nếu nghiệm hội tụ về cân bằng, hai nhánh max/min gần như trùng nhau. Khi xuất hiện nghiệm tuần hoàn, hai nhánh tách ra. Khoảng cách giữa hai nhánh thể hiện biên độ dao động của prey.

Notebook cũng vẽ bifurcation diagram theo top predator `z(t)`. Điều này giúp chứng minh dao động không chỉ xảy ra ở prey, mà lan truyền đến toàn bộ chuỗi thức ăn.

Kết quả này là bằng chứng số trực quan cho kết luận của Theorem 4.3: Hopf bifurcation tại `P3` sinh ra một họ nghiệm tuần hoàn trong miền dương.

## Vì sao phần bổ sung này cần thiết

Report mẫu có mục 4.3 nói về Hopf bifurcation tại `P3`, nhưng không có hình minh họa. Ba notebook trước đã bao phủ `P0`, `P1`, `P2`, persistence, Lyapunov và Hopf tại `P2`, nhưng chưa có mô phỏng đầy đủ cho Hopf tại `P3`.

Notebook 04 lấp đúng khoảng trống đó:

- Có cân bằng nội `P3` dương.
- Có trị riêng Jacobian 4x4 cắt trục ảo.
- Có time series trước/sau ngưỡng.
- Có phase portrait 3D.
- Có bifurcation diagram bằng max/min dài hạn.

Vì vậy phần Robustness Analysis của báo cáo sẽ đầy đủ hơn report mẫu và bám sát hơn Theorem 4.3 của paper.

## Bản giải thích chi tiết để đưa vào báo cáo

Notebook 04 là phần bổ sung quan trọng nhất nếu mục tiêu là làm báo cáo mạnh hơn report mẫu. Report mẫu có nêu Hopf tại `P3`, nhưng chưa chứng minh bằng hình số. Notebook này cung cấp toàn bộ chuỗi bằng chứng trực quan.

### 1. Khác biệt giữa Hopf tại P2 và Hopf tại P3

Hopf tại `P2` xảy ra ở cân bằng biên:

```text
P2 = (S2, x2, y2, 0)
```

Ở đó predator bậc 2 không tồn tại. Dao động chủ yếu mô tả tương tác giữa nutrient, prey và predator bậc 1.

Hopf tại `P3` xảy ra ở cân bằng nội:

```text
P3 = (S3, x3, y3, z3)
```

Tất cả thành phần đều dương. Vì vậy dao động sau Hopf tại `P3` có ý nghĩa sinh học mạnh hơn: toàn bộ chuỗi thức ăn cùng tồn tại nhưng không ở trạng thái tĩnh, mà dao động tuần hoàn.

### 2. Vì sao cần kiểm tra P3 dương?

Trước khi nói về Hopf tại `P3`, phải chắc rằng `P3` thực sự nằm trong miền nội. Nếu một biến bằng 0 hoặc âm, cân bằng đó không còn đại diện cho coexistence.

Notebook in ra `P3` tại nhiều giá trị `lambda`. Khi các giá trị đều dương, ta xác nhận rằng phân tích đang được thực hiện trên trạng thái sinh học hợp lệ:

```text
nutrient > 0
prey > 0
predator 1 > 0
predator 2 > 0
```

### 3. Ý nghĩa của Jacobian 4x4

Tại `P3`, hệ có đủ bốn biến nên Jacobian là ma trận 4x4. Ma trận này mô tả phản ứng tuyến tính của toàn bộ hệ khi bị nhiễu nhỏ khỏi cân bằng.

Nếu mọi trị riêng có phần thực âm, mọi nhiễu nhỏ đều suy giảm và `P3` ổn định. Nếu một cặp trị riêng phức có phần thực đi từ âm sang dương, nhiễu dao động sẽ được khuếch đại. Đây là cơ chế tạo ra Hopf bifurcation.

Notebook vẽ phần thực lớn nhất của trị riêng để xác định ngưỡng mất ổn định. Đồng thời vẽ phần ảo để xác nhận dao động không phải do trị riêng thực mà do cặp phức liên hợp.

### 4. Ý nghĩa của time series sau Hopf

Sau Hopf, hình time series cho thấy `S,x,y,z` dao động quanh mức cân bằng. Điều quan trọng là các biến vẫn dương. Vì vậy trạng thái sau Hopf không phải là tuyệt chủng, mà là coexistence dao động.

Diễn giải sinh học:

```text
prey tăng -> predator 1 có thêm thức ăn và tăng
predator 1 tăng -> prey bị tiêu thụ mạnh và giảm
predator 2 phản ứng với predator 1
toàn bộ chuỗi tạo thành dao động có trễ pha
```

Đây là hiện tượng thường thấy trong mô hình predator-prey: các loài không đạt cân bằng tĩnh mà dao động do quan hệ ăn-mồi.

### 5. Ý nghĩa của phase portrait 3D

Phase portrait 3D trong không gian `(x,y,z)` giúp quan sát quan hệ giữa ba quần thể sinh vật.

Trước ngưỡng Hopf, quỹ đạo co về điểm `P3`, thể hiện cân bằng ổn định. Sau ngưỡng Hopf, quỹ đạo không co về điểm mà tạo thành vòng hoặc quỹ đạo khép kín quanh `P3`. Đây là hình ảnh trực quan của nghiệm tuần hoàn.

So với time series, phase portrait cho thấy cấu trúc hình học của dao động. Nó giúp người đọc thấy rằng dao động không phải nhiễu số ngẫu nhiên, mà là một cấu trúc động học ổn định.

### 6. Ý nghĩa của bifurcation diagram tại P3

Bifurcation diagram là hình quan trọng nhất để trình bày phân nhánh. Khi vẽ:

```text
lambda -> max x(t), min x(t)
```

ta thấy:

- trước Hopf: max và min gần nhau vì nghiệm hội tụ về cân bằng;
- sau Hopf: max và min tách ra vì nghiệm dao động với biên độ khác 0.

Notebook còn vẽ max/min của `z(t)` để chứng minh predator bậc 2 cũng tham gia dao động. Điều này làm rõ rằng Hopf tại `P3` là dao động của toàn bộ food chain, không chỉ riêng prey.

### 7. Kết luận nên viết trong báo cáo

Có thể kết luận phần này như sau:

```text
Numerical simulations confirm the theoretical Hopf bifurcation at the interior equilibrium P3. As the bifurcation parameter lambda varies, a complex conjugate pair of eigenvalues of the full Jacobian crosses the imaginary axis. Before the critical value, trajectories converge to the coexistence equilibrium. After the crossing, the system exhibits sustained oscillations while all populations remain positive. This supports the theoretical claim that coexistence in the chemostat can lose stability and give rise to periodic population cycles.
```

Phiên bản tiếng Việt:

```text
Mô phỏng số xác nhận phân nhánh Hopf tại cân bằng nội P3. Khi tham số lambda thay đổi, một cặp trị riêng phức liên hợp của Jacobian 4x4 cắt trục ảo. Trước giá trị tới hạn, nghiệm hội tụ về cân bằng coexistence. Sau giá trị tới hạn, hệ xuất hiện dao động duy trì trong miền dương. Điều này cho thấy coexistence trong chemostat có thể mất ổn định và chuyển thành dao động chu kỳ của toàn bộ chuỗi thức ăn.
```
