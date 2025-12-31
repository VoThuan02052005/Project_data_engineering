"""
Làm sạch và chuẩn hóa dữ liệu thô:
- Xử lý các giá trị còn thiếu
- Chuẩn hóa giá cả và diện tích
- Phân tích ngày giờ
Output: data_processed/
"""

import numpy as np
import pandas as pd

# xử lý cột loại hình đất
def loai_hinh_dat(data):
    """
    Chuẩn hoá cột 'Loại hình đất' trong DataFrame bất động sản.

    Hàm này ánh xạ các giá trị trong cột 'Loại hình đất' về một tập
    nhãn cố định (ví dụ: Nhà biệt thự, Căn hộ chung cư, Bán đất, ...),
    dựa trên việc kiểm tra chuỗi con (substring matching).

    Nếu một giá trị không khớp với bất kỳ loại nào trong danh sách,
    giá trị gốc sẽ được giữ nguyên.

    Parameters
    ----------
    data : pandas.DataFrame
        DataFrame chứa cột 'Loại hình đất' cần được chuẩn hoá.

    Returns
    -------
    pandas.DataFrame
        DataFrame sau khi chuẩn hoá cột 'Loại hình đất'.

    Notes
    -----
    - So khớp chuỗi không phân biệt NaN (na=False).
    - Mỗi dòng chỉ được gán vào loại đầu tiên khớp trong danh sách conditions.
    - Thứ tự các điều kiện trong 'conditions' là quan trọng.
    """
    col = data['Loại hình đất']

    conditions = [
        col.str.contains("Nhà biệt thự", na=False),
        col.str.contains("Căn hộ chung cư", na=False),
        col.str.contains("Nhà mặt phố", na=False),
        col.str.contains("Bán đất", na=False),
        col.str.contains("Văn phòng", na=False),
        col.str.contains("Nhà riêng", na=False),
        col.str.contains("Condotel", na=False),
        col.str.contains("Đất nền", na=False),
        col.str.contains("Shophouse", na=False),
        col.str.contains("Nhà trọ", na=False),
        col.str.contains("Chung cư mini, căn hộ", na=False),
        col.str.contains("Kho", na=False),
        col.str.contains("Trang trại", na=False),
        col.str.contains("Cửa hàng", na=False),
        col.str.contains("Loại bất động sản khác", na=False)
    ]

    choices = [
        "Nhà biệt thự",
        "Căn hộ chung cư",
        "Nhà mặt phố",
        "Bán đất",
        "Văn phòng",
        "Nhà riêng",
        "Condotel",
        "Đất nền",
        "Shophouse",
        "Nhà trọ",
        "Chung cư mini, căn hộ",
        "Kho",
        "Trang trại",
        "Cửa hàng",
        "Loại bất động sản khác"

    ]

    data['Loại hình đất'] = np.select(conditions, choices, default=col)
    return data

# xử lý cột diện tích
def dien_tich(data):
    """
        Chuẩn hoá cột 'Diện tích' trong DataFrame bất động sản.

        Hàm chuyển các giá trị diện tích dạng chuỗi (ví dụ: "96 m²", "120,5 m²")
        về số thực (float). Các ký tự đơn vị được loại bỏ, dấu phẩy được
        chuyển thành dấu chấm.

        Các giá trị không hợp lệ hoặc không thể chuyển đổi sẽ được gán NaN.

        Parameters
        ----------
        data : pandas.DataFrame
            DataFrame chứa cột 'Diện tích'.

        Returns
        -------
        pandas.DataFrame
            DataFrame sau khi chuẩn hoá cột 'Diện tích'.
    """

    data['Diện tích'] = (
        data['Diện tích']
        .astype(str)
        .str.lower()
        .str.replace("m²", "")
        .str.replace(',', '.', regex=False)
        .pipe(pd.to_numeric, errors='coerce')
    )
    return data


# xử lý cột mức giá
def muc_gia(data):
    """
        Chuẩn hoá cột 'Mức giá' trong DataFrame bất động sản.

        Hàm chuyển các giá trị diện tích dạng chuỗi (ví dụ: "96 m²", "120,5 m²")
        về số thực (float). Các ký tự đơn vị được loại bỏ, dấu phẩy được
        chuyển thành dấu chấm.

        Các giá trị không hợp lệ hoặc không thể chuyển đổi sẽ được gán NaN.

        Parameters
        ----------
        data : pandas.DataFrame
            DataFrame chứa cột 'Diện tích'.

        Returns
        -------
        pandas.DataFrame
            DataFrame sau khi chuẩn hoá cột 'Diện tích'.
    """

    pattern = r"(?P<Gia>\d+(?:[.,]\d+)?)\s*(?P<Don_vi>.*)"

    tmp = data["Mức giá"].str.extract(pattern)

    data["Giá"] = (
        tmp["Gia"]
        .str.replace(",", ".", regex=False)
        .astype(float)
    )

    data["Đơn vị(Mức giá)"] = tmp["Don_vi"]
    return data

# xử lý cột số phòng ngủ
def so_phong_ngu(data):
    """
        Chuẩn hoá cột "Số phòng ngủ" trong DataFrame bất động sản.

        Hàm chuyển các giá trị Số phòng ngủ dạng chuỗi (ví dụ: "9 phòng", "9")
        về số nguyên int64 . loại bỏ chữ , xóa khoảng trắng.

        Các giá trị không hợp lệ hoặc không thể chuyển đổi sẽ được gán NaN.

        Parameters
        ----------
        data : pandas.DataFrame
            DataFrame chứa cột "Số phòng ngủ".

        Returns
        -------
        pandas.DataFrame
            DataFrame sau khi chuẩn hoá cột "Số phòng ngủ".
    """
    data["Số phòng ngủ"] = (
        data["Số phòng ngủ"]
        .astype(str)
        .str.replace("phòng", "")
        .str.strip()
        .pipe(pd.to_numeric, errors='coerce')
        .astype("int64")
    )
    return data

# xử lý cột số phòng tắm, vệ sinh
def so_phong_tam(data):
    """
    Chuẩn hoá cột 'Số phòng tắm, vệ sinh' trong DataFrame bất động sản.

    Hàm này chuyển các giá trị trong cột 'Số phòng tắm, vệ sinh' từ dạng
    chuỗi (ví dụ: "2 phòng", "1") sang kiểu số nguyên (Int64).
    Từ khoá "phòng" sẽ được loại bỏ, các giá trị không hợp lệ hoặc
    không thể chuyển đổi sẽ được gán NaN.

    Kiểu dữ liệu Int64 (nullable integer) được sử dụng để cho phép
    tồn tại giá trị NaN sau khi chuyển đổi.

    Parameters
    ----------
    data : pandas.DataFrame
        DataFrame chứa cột 'Số phòng tắm, vệ sinh'.

    Returns
    -------
    pandas.DataFrame
        DataFrame sau khi chuẩn hoá cột 'Số phòng tắm, vệ sinh'.
    """
    data["Số phòng tắm, vệ sinh"] = (
        data["Số phòng tắm, vệ sinh"]
        .astype(str)
        .str.replace("phòng", "")
        .str.strip()
        .pipe(pd.to_numeric, errors='coerce')
        .astype("Int64")
    )
    return data

# xử lý cột số tầng
def so_tang(data):
    """
    Chuẩn hoá cột 'Số tầng' trong DataFrame bất động sản.

    Hàm chuyển các giá trị trong cột 'Số tầng' từ dạng chuỗi
    (ví dụ: "3 tầng", "5") sang kiểu số nguyên (Int64).
    Từ khoá "tầng" được loại bỏ, các giá trị không hợp lệ hoặc
    không thể chuyển đổi sẽ được gán NaN.

    Kiểu Int64 (nullable integer) được sử dụng để cho phép
    tồn tại giá trị NaN sau khi chuẩn hoá.

    Parameters
    ----------
    data : pandas.DataFrame
        DataFrame chứa cột 'Số tầng'.

    Returns
    -------
    pandas.DataFrame
        DataFrame sau khi chuẩn hoá cột 'Số tầng'.
    """
    data["Số tầng"] = (
        data["Số tầng"]
        .astype(str)
        .str.replace("tầng", "")
        .str.strip()
        .pipe(pd.to_numeric, errors='coerce')
        .astype("Int64")
    )
    return data

# xử lý cột mặt tiền
def mat_tien(data):
    """
    Chuẩn hoá cột 'Mặt tiền' trong DataFrame bất động sản.

    Hàm chuyển các giá trị trong cột 'Mặt tiền' từ dạng chuỗi
    (ví dụ: "4m", "5.5 m") sang kiểu số thực (float).
    Ký tự đơn vị "m" được loại bỏ, các giá trị không hợp lệ
    hoặc không thể chuyển đổi sẽ được gán NaN.

    Parameters
    ----------
    data : pandas.DataFrame
        DataFrame chứa cột 'Mặt tiền'.

    Returns
    -------
    pandas.DataFrame
        DataFrame sau khi chuẩn hoá cột 'Mặt tiền'.
    """
    data["Mặt tiền"] = (
        data["Mặt tiền"]
        .astype(str)
        .str.replace("m", "")
        .str.strip()
        .pipe(pd.to_numeric, errors='coerce')
    )
    return data

# xử lý cột đường vào
def duong_vao(data):
    """
    Chuẩn hoá cột 'Đường vào' trong DataFrame bất động sản.

    Hàm chuyển các giá trị trong cột 'Đường vào' từ dạng chuỗi
    (ví dụ: "3m", "5.5 m") sang kiểu số thực (float).
    Ký tự đơn vị "m" được loại bỏ, các giá trị không hợp lệ
    hoặc không thể chuyển đổi sẽ được gán NaN.

    Parameters
    ----------
    data : pandas.DataFrame
        DataFrame chứa cột 'Đường vào'.

    Returns
    -------
    pandas.DataFrame
        DataFrame sau khi chuẩn hoá cột 'Đường vào'.
    """
    data["Đường vào"] = (
        data["Đường vào"]
        .astype(str)
        .str.replace("m", "")
        .str.strip()
        .pipe(pd.to_numeric, errors='coerce')
    )
    return data

# xử lý cột ngày đăng
def ngay_dang(data):
    """
    Chuẩn hoá cột 'Ngày đăng' trong DataFrame bất động sản.

    Hàm chuyển các giá trị ngày đăng từ nhiều định dạng chuỗi
    (ví dụ: '05-06-2025', '24/06/2025') về kiểu datetime64.
    Các giá trị không hợp lệ sẽ được gán NaT.

    Parameters
    ----------
    data : pandas.DataFrame

    Returns
    -------
    pandas.DataFrame
    """
    data["Ngày đăng"] = (
        data["Ngày đăng"]
        .astype(str)
        .str.strip()
        .replace({"nan": None})
    )

    data["Ngày đăng"] = pd.to_datetime(
        data["Ngày đăng"],
        dayfirst=True,        # RẤT QUAN TRỌNG cho dữ liệu VN
        errors="coerce"
    )

    return data


