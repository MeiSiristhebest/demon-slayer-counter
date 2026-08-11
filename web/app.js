document.addEventListener('DOMContentLoaded', () => {
  const DEMON_SLAYER_CHARS = [
    { num: '0', name: '灶门炭治郎', pose: '3/4 侧身坚毅站姿，阳光温和微笑' },
    { num: '1', name: '灶门祢豆子', pose: '软萌鸭子蹲姿，斜贴脸捧牌眨眼' },
    { num: '2', name: '我妻善逸', pose: '膝盖内八字打颤，瀑布流泪哭唧唧' },
    { num: '3', name: '嘴平伊之助', pose: '单脚霸气踩石，野猪头套仰天咆哮' },
    { num: '4', name: '栗花落香奈乎', pose: '优雅侧身抛硬币，恬静轻微笑' },
    { num: '5', name: '富冈义勇', pose: '侧身单手藏袖，死鱼眼冷酷夹牌' },
    { num: '6', name: '胡蝶忍', pose: '单脚踮立展开蝶翼，闭眼眯眯甜笑' },
    { num: '7', name: '炼狱杏寿郎', pose: '双腿豪迈跨开，昂头大笑霸气向前' },
    { num: '8', name: '甘露寺蜜璃', pose: 'S型扭腰前倾，粉红脸颊爱心眼' },
    { num: '9', name: '时透无一郎', pose: '屈膝发呆坐姿，薄荷绿双眼仰望天空' }
  ];

  let currentFormat = 'webp';
  let isAnimated = true;

  // DOM Elements
  const counterInput = document.getElementById('counterInput');
  const btnInc = document.getElementById('btnInc');
  const btnRandom = document.getElementById('btnRandom');
  const counterStage = document.getElementById('counterStage');
  const digitCountMeta = document.getElementById('digitCountMeta');
  const characterGallery = document.getElementById('characterGallery');
  const animateToggle = document.getElementById('animateToggle');
  const formatRadios = document.querySelectorAll('input[name="imgFormat"]');
  const codeMarkdown = document.getElementById('codeMarkdown');
  const codeHTML = document.getElementById('codeHTML');
  const copyBtns = document.querySelectorAll('.btn-copy');
  const toast = document.getElementById('toast');

  // Render Counter Stage
  function renderCounter() {
    let val = counterInput.value.replace(/[^0-9]/g, '');
    if (!val) val = '0';
    
    counterStage.innerHTML = '';
    const digits = val.split('');

    digits.forEach((digit, idx) => {
      const card = document.createElement('div');
      card.className = `digit-card-wrapper ${isAnimated ? 'animated' : ''}`;
      card.style.animationDelay = `${(idx % 5) * 0.15}s`;

      const img = document.createElement('img');
      img.src = `assets/demon-slayer/${digit}.${currentFormat}`;
      img.alt = `Digit ${digit}`;
      img.className = 'digit-card-img';

      card.appendChild(img);
      counterStage.appendChild(card);
    });

    digitCountMeta.textContent = `共 ${digits.length} 位数字`;
    updateEmbedCodes();
  }

  // Render Gallery
  function renderGallery() {
    characterGallery.innerHTML = '';

    DEMON_SLAYER_CHARS.forEach(item => {
      const card = document.createElement('div');
      card.className = 'gallery-card';

      card.innerHTML = `
        <div class="gallery-card-img-wrap">
          <img src="assets/demon-slayer/${item.num}.${currentFormat}" alt="${item.name}" class="gallery-card-img">
        </div>
        <span class="gallery-card-num">${item.num}</span>
        <h3 class="gallery-card-name">${item.name}</h3>
        <p class="gallery-card-pose">${item.pose}</p>
      `;

      characterGallery.appendChild(card);
    });
  }

  // Update Embed Codes
  function updateEmbedCodes() {
    const markdown = `[![Demon Slayer View Counter](https://your-counter.vercel.app/api/counter?name=YOUR_GITHUB_USERNAME)](https://github.com/YOUR_GITHUB_USERNAME)`;
    const html = `<img src="https://your-counter.vercel.app/api/counter?name=YOUR_GITHUB_USERNAME" alt="Demon Slayer Counter" />`;

    codeMarkdown.textContent = markdown;
    codeHTML.textContent = html;
  }

  // Event Listeners
  counterInput.addEventListener('input', () => {
    counterInput.value = counterInput.value.replace(/[^0-9]/g, '');
    renderCounter();
  });

  btnInc.addEventListener('click', () => {
    let num = parseInt(counterInput.value || '0', 10);
    num += 1;
    counterInput.value = num.toString();
    renderCounter();
  });

  btnRandom.addEventListener('click', () => {
    const randomNum = Math.floor(Math.random() * 9000000000) + 1000000000;
    counterInput.value = randomNum.toString();
    renderCounter();
  });

  animateToggle.addEventListener('change', (e) => {
    isAnimated = e.target.checked;
    renderCounter();
  });

  formatRadios.forEach(radio => {
    radio.addEventListener('change', (e) => {
      currentFormat = e.target.value;
      renderCounter();
      renderGallery();
    });
  });

  copyBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      const targetId = btn.dataset.target;
      const textToCopy = document.getElementById(targetId).textContent;

      navigator.clipboard.writeText(textToCopy).then(() => {
        showToast('代码已成功复制到剪贴板！');
      }).catch(() => {
        showToast('复制失败，请手动选择复制。');
      });
    });
  });

  function showToast(msg) {
    toast.textContent = msg;
    toast.classList.add('show');
    setTimeout(() => {
      toast.classList.remove('show');
    }, 2500);
  }

  // Initial Load
  renderCounter();
  renderGallery();
});
