# Menggunakan image dasar resmi Python
FROM python:3.9-slim

# Menetapkan direktori kerja di dalam container
WORKDIR /usr/src/app

# Menyalin file requirements.txt ke dalam container
COPY requirements.txt ./

# Menginstal dependensi dari requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Menyalin semua file dari direktori saat ini ke dalam container
COPY . .

# Menjalankan shell sebagai default command
CMD ["sh"]
