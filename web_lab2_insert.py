import sqlite3

connection = sqlite3.connect('my_database.db')
cursor = connection.cursor()

#заполням таблицу администраторов данными 5 человек
cursor.execute('''
INSERT INTO admin (admin_id, admin_name, login, password) 
VALUES (11, 'John Smith', 'john_admin', 'admin123'),
       (12, 'Emily Johnson', 'emily_admin', 'admin456'),
       (13, 'Michael Davis', 'michael_admin', 'admin789'),
       (14, 'Jessica Brown', 'jessica_admin', 'admin101'),
       (15, 'Chris Wilson', 'chris_admin', 'admin202')''')
print(cursor.fetchall())
#заполням таблицу клиентов данными 20 человек
cursor.execute('''INSERT INTO client (client_id, client_name, login, password)
VALUES (1, 'Alice Johnson', 'alice_client', 'client123'),
       (2, 'Bob Smith', 'bob_client', 'client456'),
       (3, 'Eva Davis', 'eva_client', 'client789'),
       (4, 'Tom Brown', 'tom_client', 'client101'),
       (5, 'Olivia Wilson', 'olivia_client', 'client202'),
       (6, 'Sophia Thompson', 'sophia123', 'pass123'),
       (7, 'Daniel White', 'danielw', 'dwhite'),
       (8, 'Olivia Harris', 'olivia87', 'harris87'),
       (9, 'James Martin', 'james_m', 'jamemar'),
       (10, 'Emma Scott', 'emmas', 'scotty21'),
       (11, 'Liam Clark', 'liamc', 'clark2021'),
       (12, 'Ava Lewis', 'avalew', 'lewisava'),
       (13, 'Mia Lee', 'mial', 'meemeel'),
       (14, 'Noah King', 'noahk', 'kingnoah'),
       (15, 'Isabella Green', 'izzy', 'green4'),
       (16, 'Lucas Walker', 'lucasw', 'walkerluc'),
       (17, 'Amelia Hall', 'ameliah', 'hallam'),
       (18, 'Ethan Young', 'ethany', 'youngmoney'),
       (19, 'Charlotte Wright', 'charlottew', 'wrightchar'),
       (20, 'Mason Adams', 'masona', 'adams21')''')
print(cursor.fetchall())
#заполням таблицу фотостудий данными 3 пространств
cursor.execute('''
INSERT INTO photostudio (photostudio_id, studio_name)
VALUES (1, 'Focus Photography Studio'),
       (2, 'Creative Capture Studio'),
       (3, 'Elegant Moments Studio')''')

#заполням таблицу 30 записями
cursor.execute('''
INSERT INTO orders (order_id, admin_id, photostudio_id, date, time_begin, time_end, price, client_id)
VALUES (1, 1, 1, '2023-01-15', '10:00:00', '11:00:00', 2000, 1),
       (2, 1, 2, '2023-02-20', '11:00:00', '12:00:00', 1800, 2),
       (3, 2, 3, '2023-03-25', '12:00:00', '13:00:00', 2200, 3),
       (4, 2, 1, '2023-04-11', '13:00:00', '14:00:00', 2000, 4),
       (5, 3, 2, '2023-05-30', '14:00:00', '15:00:00', 1900, 5),
       (6, 3, 3, '2023-06-05', '15:00:00', '16:00:00', 2100, 1),
       (7, 4, 1, '2023-07-17', '16:00:00', '17:00:00', 2000, 2),
       (8, 4, 2, '2023-08-22', '17:00:00', '18:00:00', 1800, 3),
       (9, 5, 3, '2023-09-10', '18:00:00', '19:00:00', 2200, 4),
       (10, 5, 1, '2023-10-12', '19:00:00', '20:00:00', 2000, 5),
       (11, 1, 2, '2023-11-28', '10:00:00', '11:00:00', 1900, 1),
       (12, 1, 3, '2023-12-02', '11:00:00', '12:00:00', 2100, 2),
       (13, 2, 1, '2024-01-06', '12:00:00', '13:00:00', 2000, 3),
       (14, 2, 2, '2024-02-14', '13:00:00', '14:00:00', 1800, 4),
       (15, 3, 3, '2024-03-19', '14:00:00', '15:00:00', 2200, 5),
       (16, 3, 1, '2024-04-25', '15:00:00', '16:00:00', 2000, 1),
       (17, 4, 2, '2024-05-29', '16:00:00', '17:00:00', 1900, 2),
       (18, 4, 3, '2024-06-30', '17:00:00', '18:00:00', 2100, 3),
       (19, 5, 1, '2024-07-17', '18:00:00', '19:00:00', 2000, 4),
       (20, 5, 2, '2024-08-22', '19:00:00', '20:00:00', 1800, 5),
       (21, 1, 3, '2024-09-02', '10:00:00', '11:00:00', 2200, 1),
       (22, 1, 1, '2024-10-14', '11:00:00', '12:00:00', 2000, 2),
       (23, 2, 2, '2024-11-25', '12:00:00', '13:00:00', 1900, 3),
       (24, 2, 3, '2024-12-30', '13:00:00', '14:00:00', 2100, 4),
       (25, 3, 1, '2025-01-21', '14:00:00', '15:00:00', 2000, 5),
       (26, 3, 2, '2025-02-28', '15:00:00', '16:00:00', 1800, 1),
       (27, 4, 3, '2025-03-15', '16:00:00', '17:00:00', 2200, 2),
       (28, 4, 1, '2025-04-20', '17:00:00', '18:00:00', 2000, 3),
       (29, 5, 2, '2025-05-05', '18:00:00', '19:00:00', 1900, 4),
       (30, 5, 3, '2025-06-07', '19:00:00', '20:00:00', 2100, 5);''')
print(cursor.fetchall())
#заполням таблицу 30 записями
cursor.execute('''
INSERT INTO service_order (service_id, service_name, order_id, price)
VALUES 
(1, 'photographer', 1, 2000),    
(2, 'additional', 1, 1000),    
(3, 'dressroom', 1, 500),   
(4, 'visagiste', 1, 1200),    
(5, 'stylist', 1, 1000),    
(6, 'photographer', 2, 2000),   
(7, 'additional', 2, 1000),    
(8, 'dressroom', 2, 500),    
(9, 'visagiste', 2, 1200),    
(10, 'stylist', 2, 1000),    
(11, 'photographer', 3, 2000),    
(12, 'additional', 3, 1500),    
(13, 'dressroom', 3, 500),   
(14, 'visagiste', 3, 1200),    
(15, 'stylist', 3, 1000),    
(16, 'photographer', 4, 2000),    
(17, 'additional', 4, 1000),   
(18, 'dressroom', 4, 500),   
(19, 'visagiste', 4, 1200),  
(20, 'stylist', 4, 1000),    
(21, 'photographer', 5, 2000),  
(22, 'additional', 5, 1500),    
(23, 'dressroom', 5, 500),    
(24, 'visagiste', 5, 1200),    
(25, 'stylist', 5, 1000),  
(26, 'photographer', 6, 2000),  
(27, 'additional', 6, 1000),  
(28, 'dressroom', 6, 500),  
(29, 'visagiste', 6, 1200),  
(30, 'stylist', 6, 1000),  
(31, 'photographer', 7, 2000),  
(32, 'additional', 7, 1500),  
(33, 'dressroom',7, 500),  
(34, 'visagiste', 7, 1200),  
(35, 'stylist', 7, 1000),  
(36, 'photographer', 8, 2000),  
(37, 'additional', 8, 1000),  
(38, 'dressroom', 8, 500),  
(39, 'visagiste', 8, 1200),  
(40, 'stylist', 8, 1000);''')
print(cursor.fetchall())
connection.commit()
cursor.execute('''SELECT admin_name FROM admin''')
print(cursor.fetchall())
# Сохраняем изменения и закрываем соединение
connection.commit()
connection.close()
