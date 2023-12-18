jQuery(document).ready(function ($) {
	let mobileMenuWidth = 1024, //mobile menu delimeter
		scrollMenuHeight = parseInt($('.wrapper').css('--scroll-menu-height'));

	//fixed-menu
	$(window).on("scroll", function () {
		menuOnScroll();
	});
	menuOnScroll();

	function menuOnScroll() {
		if ($(this).scrollTop() > 0) {
			$(".wrapper").addClass("scroll");
		} else {
			$(".wrapper").removeClass("scroll");
		}

		$(window).on('DOMMouseScroll mousewheel', function (event) {
			if (event.originalEvent.detail > 0 || event.originalEvent.wheelDelta < 0) {
				$(".wrapper").removeClass('scroll-up');
			} else {
				$(".wrapper").addClass('scroll-up');
			}
		});
	}


	function mobileMenu(selector) {

		let menu = $(selector);
		let button = menu.find('#hamburger');
		let overlay = menu.find('#menu-overlay');

		button.on('click', () => toggleMenu());
		overlay.on('click', () => toggleMenu());

		function toggleMenu() {
			if ($(window).width() <= mobileMenuWidth) {
				menu.toggleClass('menu-active');

				if (menu.hasClass('menu-active')) {
					$('body').css('overflow', 'hidden');
				} else {
					$('body').css('overflow', 'visible');
					$('.submenu-child').hide();
					$('.submenu > a').removeClass('focus');
				}
			}
		}
	}

	//submenu
	function submenuClick() {
		$('.submenu > a').click(function (e) {
			if ($(window).width() <= mobileMenuWidth) {
				if (!($(this).hasClass('focus'))) {
					e.preventDefault();
					$('.submenu > a').removeClass('focus');
					$(this).addClass('focus');
					$(this).next('.submenu-child').fadeToggle(500);
					$(this).parents('.submenu').toggleClass('open');
				}
			}
		});
		$('.submenu > span').click(function (e) {
			if ($(window).width() <= mobileMenuWidth) {
				$(this).next('.submenu-child').fadeToggle(500);
				$(this).parents('.submenu').toggleClass('open');
			}
		});
	}

	//init menu
	mobileMenu('#header-menu');
	submenuClick();

	//smooth scroll
	$(".js-scroll-to").on("click", function () {
		const anchor = this.hash;
		const top = $(`${anchor}`).offset().top - parseInt($(`${anchor}`).css('marginTop'));
		$('body,html').animate({
			scrollTop: top - scrollMenuHeight
		}, 750);
	});

	//slider
	function initShowcaseSlider() {
		$('.js-showcase-slider').slick({
			autoplay: true,
			autoplaySpeed: 3000,
			fade: true,
			slidesToShow: 1,
			slidesToScroll: 1,
			arrows: false,
			dots: true,
		});
	}
	initShowcaseSlider();

	function initProjectsSlider() {
		$('.js-projects-slider').slick({
			slidesToShow: 3,
			slidesToScroll: 1,
			arrows: true,
			prevArrow: '<div class="sliderPrev"></div>',
			nextArrow: '<div class="sliderNext"></div>',
			responsive: [
				{
					breakpoint: 769,
					settings: {
						slidesToShow: 2
					}
				},
				{
					breakpoint: 601,
					settings: {
						slidesToShow: 1
					}
				}
			]
		});
	}
	initProjectsSlider();

	function initReviewsSlider() {
		$('.js-reviews-slider').slick({
			autoplay: true,
			autoplaySpeed: 3000,
			fade: true,
			slidesToShow: 1,
			slidesToScroll: 1,
			arrows: false,
			dots: true,
		});
	}
	initReviewsSlider();

	function initProjectItemSlider() {
		$('.js-project-item-slider-for').slick({
			arrows: true,
			prevArrow: '<div class="sliderPrev"></div>',
			nextArrow: '<div class="sliderNext"></div>',
			fade: true,
		});
		$(".js-project-item-slider-nav > div").click(function (e) {
			e.preventDefault();
			slideIndex = $(this).index();
			$('.js-project-item-slider-for').slick('slickGoTo', parseInt(slideIndex));
		});
	}
	initProjectItemSlider();

	// how-it-works tabs
	if (document.querySelector('.js-how-it-works-tabs')) {

		const mediaQuery = '(max-width: 767px)';
		const mediaQueryList = window.matchMedia(mediaQuery);
		const tabs = document.querySelector('.js-how-it-works-tabs');
		const slider = document.querySelector('.js-how-it-works-slider');
		const tabsTrigger = tabs.querySelectorAll('.how-it-works__trigger');
		const tabsContent = tabs.querySelectorAll('.how-it-works__tabs-content');

		function hideTabsContent() {
			tabsContent.forEach(item => {
				item.setAttribute('hidden', '');
				item.classList.remove('fade');
			});

			tabsTrigger.forEach(item => {
				item.classList.remove('active');
			});
		}
		function showTabsContent(i = 0) {
			tabsContent[i].classList.add('fade');
			tabsContent[i].removeAttribute('hidden');
			tabsTrigger[i].classList.add('active');
		}
		function hendler() {
			tabsTrigger.forEach((item, i) => {
				if (this == item) {
					hideTabsContent();
					showTabsContent(i);
				}
			});
		}
		function initTabs() {
			hideTabsContent();
			showTabsContent();
			tabsTrigger.forEach(item => {
				item.addEventListener('click', hendler);
			});
		}
		function destroyTabs() {
			tabsTrigger.forEach(item => {
				item.removeEventListener('click', hendler);
			});
			tabsContent.forEach(item => {
				item.removeAttribute('hidden');
			});
		}

		function howItWorksSlider() {
			$('.js-how-it-works-slider').slick({
				fade: true,
				slidesToShow: 1,
				slidesToScroll: 1,
				arrows: false,
				dots: true,
			});
		}

		mediaQueryList.addEventListener('change', (e) => {
			if (!mediaQueryList.matches) {
				initTabs();
				if ($(slider).hasClass('slick-initialized')) {
					$(slider).slick('unslick');
				}
			} else {
				destroyTabs();
				if (!$(slider).hasClass('slick-initialized')) {
					howItWorksSlider();
				}
			}
		});

		if (!mediaQueryList.matches) {
			initTabs();
			if ($(slider).hasClass('slick-initialized')) {
				$(slider).slick('unslick');
			}
		} else {
			destroyTabs();
			if (!$(slider).hasClass('slick-initialized')) {
				howItWorksSlider();
			}
		}
	}

	// video-block
	const playVideoBtn = document.querySelectorAll('.js-video-play');
	if (playVideoBtn) {
		playVideoBtn.forEach(item => {
			item.addEventListener("click", handlePlayBtn, { once: true });
		})

		async function playVideo(videoElem) {
			try {
				await videoElem.play();
			} catch (err) { }
		}

		function handlePlayBtn() {
			const videoElem = this.closest('.video-block').querySelector('video');
			this.classList.add('hide');
			videoElem.setAttribute('controls', 'true');
			playVideo(videoElem);
		}
	}

	// like-file
	document.querySelectorAll('.js-like-file input[type="file"]').forEach(item => {
		item.addEventListener('change', function () {
			let fileNames = [];
			const uploadList = this.closest('.js-like-file').querySelector('.js-like-file__upload-list');
			for (let i = 0; i < this.files.length; i++) {
				fileNames.push(this.files[i].name);
			}
			if (this.value != '') {
				uploadList.innerHTML = fileNames.join(', ');
			} else {
				uploadList.innerHTML = '';
			}
		});
	});

	// Before-after slider 
	//NOTE use .cocoen class for call slider for element
	if (document.querySelector('.cocoen')) {
		document.querySelectorAll('.cocoen').forEach(item => {
			Cocoen.create(item);
		});

	}

	//aos animations init
	AOS.init({
		disable: (
			/bot|crawler|spider|crawling/i.test(navigator.userAgent)
			|| window.matchMedia("(prefers-reduced-motion: reduce)").matches
		),
	});

});
