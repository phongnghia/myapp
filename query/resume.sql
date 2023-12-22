/*
-- Query: SELECT * FROM myresume_django.myresume_resume
LIMIT 0, 1000

-- Date: 2022-09-03 23:57
*/
INSERT INTO myresume_resume  (id,name,birthday,phone,address,email,story,position,image,work_exp,part_project,gpa,university,linked) VALUES (1,'Nghia Pham','1999-08-10','0356156445','Mo Duc, Quang Ngai, Viet Nam','nghiaphamhong99@gmail.com','Hello everyone, I was born and raised in Quang Ngai province, I studied at Pham Van Dong high school and a university of the same name in my hometown Quang Ngai. I graduated from university in June of 2021. I have 2 years experience in Java developer at TMA solution Binh Dinh','Software Engineer','resume-images/avatar_4huorvJ.jpg',2.7,2,3.15,'Pham Van Dong','https://www.linkedin.com/in/nghia-pham-a641621b1');



/*
-- Query: SELECT * FROM myresume_django.myresume_otherimage
LIMIT 0, 1000

-- Date: 2022-09-03 23:58
*/
INSERT INTO myresume_otherimage (id,image,name_id) VALUES (1,'resume-image/other-image.png',1);
INSERT INTO myresume_otherimage (id,image,name_id) VALUES (3,'resume-image/DSCF4558.JPG',1);



/*
-- Query: SELECT * FROM myresume_django.myresume_detailtechnical
LIMIT 0, 1000

-- Date: 2022-09-03 23:57
*/
INSERT INTO myresume_detailtechnical (id,tech_exp,tech_level,name_id,tech_name_id) VALUES (1,1,3,1,1);
INSERT INTO myresume_detailtechnical (id,tech_exp,tech_level,name_id,tech_name_id) VALUES (3,0,2,1,4);
INSERT INTO myresume_detailtechnical (id,tech_exp,tech_level,name_id,tech_name_id) VALUES (4,0,2,1,3);
INSERT INTO myresume_detailtechnical (id,tech_exp,tech_level,name_id,tech_name_id) VALUES (6,0,3,1,5);
INSERT INTO myresume_detailtechnical (id,tech_exp,tech_level,name_id,tech_name_id) VALUES (7,2,3,1,6);
INSERT INTO myresume_detailtechnical (id,tech_exp,tech_level,name_id,tech_name_id) VALUES (8,1.5,2,1,7);



/*
-- Query: SELECT * FROM myresume_django.myresume_companiesworked
LIMIT 0, 1000

-- Date: 2022-09-03 23:59
*/
INSERT INTO myresume_companiesworked (id,company_exp,company_name_id,name_id) VALUES (2,2.7,3,1);



/*
-- Query: SELECT * FROM myresume_django.myresume_project
LIMIT 0, 1000

-- Date: 2022-09-03 23:58
*/
INSERT INTO myresume_project (id,project_name,project_des,project_image,name_id) VALUES (1,'Nokia','Device & Network','resume-image/nokia.png',1);
INSERT INTO myresume_project (id,project_name,project_des,project_image,name_id) VALUES (2,'Internship project','Employee Management','resume-image/manage-staff.png',1);