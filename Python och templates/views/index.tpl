<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<title>Nabo</title>
		<link rel="stylesheet" href="/static/style.css">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
	</head>

	<header>
		Nabologga här

		
	</header>

	<body>
		<div id="signin">

		<p>SIGN IN</p>	
		<form action="/index/board/" method="POST">
		<form class="form">
		<p class="email">
			<input required type="text" name="email" id="email" placeholder="Email" />			
		</p>

		<p class="password">
			<input required type="password" name="pwd_1" id="password" placeholder="Password" />	
		</p>

		
		<p class="submit">
			<input type="submit" value="Sign in" />
		</p>
		</form>
		</div>


		<div id="signUp">

		<form action="/Nabo/" method="POST" class="form">
		<p class="email">
			<input required type="text" name="email" id="email" placeholder="Email" />			
		</p>

		<p class="password">
			<input required type="password" required pattern="(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{6,}" name="pwd1" name="pwd_1" id="password" placeholder="Password" onchange="form.pwd2.pattern = this.value;>	
		</p>

		<p class="password">
			<input type="password" required pattern="(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{6,}" name="pwd_2" id="password" placeholder="Confirm password">	
		</p>
		
		<p class="submit">
			<input type="submit" value="Sign in">
		</p>
		</form>
		</div>


	</body>

	<footer>
		<a href="contact.html">Kontakta oss</a>
		<a href="about.html">Om Nabo</a>
		<a href="help.html">Hjälp</a>
	</footer>
</html>


