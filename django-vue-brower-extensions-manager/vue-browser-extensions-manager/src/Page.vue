<template>

	<header class="side-margin">

			<article class="vert-middle">
				<span class="crop-header-logo vert-middle">
					<img src="./assets/images/logo.svg" alt="extensions-logo">
				</span>
				<h2 class='header-title vert-middle'>Extensions</h2>
			</article>

			<article class="vert-middle">
				<input type="checkbox" class="mode-toggle" id="mode-toggle">
				<label class="mode-toggle vert-middle horz-middle" for="mode-toggle">
						<img src="./assets/images/icon-sun.svg">
				</label>
			</article>

	</header>

		<section class="side-margin">

				<article class="horz-middle vert-middle">
					<h1>Extensions List</h1>	
				</article>
				<article class="horz-middle vert-middle">
					<article class="radio-article" @change="convertJSONtoCards">
					
							<input type="radio" class="sort-radio" id="all" name="sort-radio" checked>
							<label class="sort-radio" for="all">
								 All
							</label>

							<input type="radio" class="sort-radio" id="active" name="sort-radio">
							<label class="sort-radio" for="active">
               Active
							</label>

							<input type="radio" class="sort-radio" id="inactive" name="sort-radio">
							<label class="sort-radio" for="inactive">
               Inactive
							</label>				

					</article>
				</article>

		</section>

</template>
