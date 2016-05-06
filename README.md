# snps-photo-album
Synopsys Python SIG 兴趣小组项目

## 1. 用户模块 ##

	
- index
	- 首页


- login 
	- 登入

	
- logout
	- 登出


- register
	- 注册 (不用做)
	

- find_passwd 
	- 找回密码
	

- user_id
	- 查看个人首页（已经登入）	
	- 查看别人首页（未登入）
	


- user_userid/profile/
	
	- 查看个人资料



- user_userid/profile/edit

	- 修改个人资料





## 2. 照片模块 user ==> post==> photo

- user_userid/

		==> 查看用户的所有的 post 照片

		==> 同时也能批量下载同一个post 的照片



- user_userid/new

		==> 新建一个post



- user_userid/edit

		==> 修改一个完整的post



- user_userid/post_delete

		==> 删除整个post


- user_userid/post_postid/

		==>查看一个具体的post


- user_userid/post_postid/edit

		==> 修改某个post 的信息, 比如删除某张照片，新加某张照片，修改post 名字

	
- user_userid/post_postid/photo_photoid/

		==> 查看一张照片


-	user_userid/post_postid/photo_photoid/edit

		==> 修改一张照片，比如给这张照片添加备注，圈人等等


- 同时对照片模块提供可供选择的tag，比如travel 或者 study之类，可以对照片进行筛选等，放在edit 里面进行操作


## 3. 管理模块 #

- admin

		==> 超级管理员
		
		==> Django 自带的即可？



## 4. 数据库模块 (Model)


## 5. 输出模板模块 (Template)




# action item:

## photo, photo_edit
	* title, tag, 圈人（TODO），like, comment,
	* Henry Qi <jingqi@synopsys.com>;
	* table class: Photo, Tag, Comments, Like
	
## post, post_edit
	* delete photo， add new photo， post title， post tag， post like， post comment
	* tag，like，comment，title， 对于post 和photo的重用，继承
	* Mingchao Ji <mcji@synopsys.com>; 
	* table class: Post
	
## user/ user_edit
	* delete a post, add new post，批量上传照片功能
	* 考虑对于 add， delete 在post 和photo层级的重用，继承
	* add photo 和add post，
	* daniel Xu

## user profile
	* nickname，pic，info，
	* Yifei Huang <yfhuang@synopsys.com>; 
## model
	* yaodong Hu
## index
	* Liang Zhu <liangzh@synopsys.com>; 
## admin 
	* Lin Chen <linchen@synopsys.com>
	* yifei Huang


