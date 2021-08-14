from flask_admin.form import DatePickerWidget
from flask_wtf import FlaskForm
from wtforms import StringField , PasswordField , SubmitField , SelectField , DateField
from wtforms.validators import DataRequired


class UserLoginForm(FlaskForm):
    username = StringField('Username/SĐT', validators=[DataRequired()])
    password = PasswordField('Mật khẩu', validators=[DataRequired()])
    submit = SubmitField('Đăng nhập')


class UserRegisterForm(FlaskForm):
    name = StringField('Họ và tên', validators=[DataRequired()])
    gender = SelectField('Giới tính', choices=[('Nam', 'Nam'), ('', 'Nữ'),
                                                ('Other', 'Other')]
                                        ,validators=[DataRequired("Vui lòng chọn ít nhất một lựa chọn")])
    phone_no = StringField('SĐT')
    date_of_birth = DateField('Ngày sinh', widget=DatePickerWidget())
    status = SelectField('Bạn là', choices=[('Sinh viên y, dược/bác sĩ', 'Sinh viên y, dược'),
                                                           ('Người dân', 'dân')]
                                , validators=[DataRequired("Vui lòng chọn ít nhất một lựa chọn")])
    purpose = SelectField('Mục đích sử dụng website', choices=
                                [('Tư vấn, giải đáp các câu hỏi về phòng, chữa Covid-19','tư vấn'),
                                 ('Tìm hiểu thêm thông tin về phòng, chữa Covid', 'tìm hiểu covid'),
                                ('Tìm nơi cung cấp thực phẩm uy tín, giá cả phải chăng', 'tìm thực phẩn'),
                                 ('Cung cấp thực phẩm chất lượng, phù hợp với nhu cầu người dân','cung cấp'),
                                 ('Other', 'other')]
                                ,validators=[DataRequired("Vui lòng chọn ít nhất một lựa chọn")])
    submit = SubmitField('Đăng ký')

