# Rookie2 Portfolio Site Guide

이 문서는 Rookie2 Portfolio 사이트 작업을 이어받기 위한 가이드입니다. 다음 작업자가 이 파일만 보더라도 현재 `index.html`이 어떤 의도로 구성되었는지, 앞으로 어떤 기준으로 작업해야 하는지 이해할 수 있게 유지합니다.

## 현재 파일 구조

- `index.html`: 현재 랜딩 페이지 전체 구조, 스타일, 스크롤/비디오 제어 스크립트가 들어 있는 단일 HTML 파일입니다.
- `assets/images/HeroImg.png`: Hero 기본 배경 이미지입니다.
- `assets/images/HeroImg_Color.png`: Hero 위에 얹는 컬러 효과 레이어입니다.
- `assets/images/Intro_mv_poster.png`: Intro motion 영상 poster 이미지입니다.
- `assets/images/NaverLabsMark.svg`: Hero 하단 NAVER LABS 로고입니다.
- `assets/images/visual-principles/card-principles-graphic.svg`: Visual Principles 1번 카드의 벡터 그래픽 이미지입니다. 배경이 보이지 않도록 Figma의 `Subtract` 벡터를 SVG로 가져왔고, 카드 내부 텍스트는 HTML/CSS로 따로 얹습니다.
- `assets/images/visual-principles/card-vision-grid.png`: Visual Principles 2번 카드의 이미지 그리드입니다. 카드 하나당 하나의 이미지 파일로 관리한다는 원칙에 맞춰 Figma 이미지 타일 10개를 투명 배경의 한 장 PNG로 합성했습니다.
- `assets/images/visual-principles/card-understood-visual.jpg`: Visual Principles 3번 카드 `Designed to Be Understood`의 배경 비주얼 이미지입니다.
- `assets/images/visual-principles/card-expressive-gaze-bg.png`: Visual Principles 4번 카드 `Expressive Gaze`의 배경 이미지입니다. 흰색 선 5개는 이미지에 굽지 않고 HTML/CSS로 얹습니다.
- `assets/images/visual-principles/card-future-form.png`: Visual Principles 5번 카드의 전체 이미지입니다.
- `assets/fonts/a-type/AType-Bold.otf`: Hero 타이틀 `Rookie2`에 사용하는 A Type 웹폰트입니다. 사이트에서 쓰는 두께만 `assets` 아래에서 관리합니다.
- `assets/media/Intro_mv.mp4`: 스크롤에 따라 재생/역재생되는 Intro motion 영상입니다.
- `assets/content/intro.json`: Intro 문구의 `en`, `ko` 보관용 콘텐츠입니다. 현재 화면은 HTML에 직접 박힌 영문을 사용하지만, 나중에 한글화할 때 이 파일을 기준으로 다시 적용합니다.
- `History/index_20260619_001030.html`: 2026-06-19 00:10 기준, 공통 타이포그래피 토큰 적용 직전의 `index.html` 스냅샷입니다.

## 2026-06-17 최종 점검

오늘 작업 기준으로 확정된 내용:

- `index.html`에 favicon SVG data URL을 직접 포함했습니다.
- Hero 타이틀 폰트는 `assets/fonts/a-type/AType-Bold.otf`를 `@font-face`로 로드합니다. 루트의 `A type/` 원본 폴더는 사이트 자산으로 쓰지 않고 Git 추적에서도 제외합니다.
- 터치 환경의 Hero 배경은 `position: absolute`로 전환합니다. 이전처럼 최상단 pull-down을 `touchmove`에서 막는 방식은 다시 사용하지 않습니다.
- Visual Principles 카드 폭은 모든 반응형 지점에서 `var(--section-width)`를 사용합니다. 활성 카드, 타이틀, 인디케이터의 좌측 기준선은 항상 같아야 합니다.
- Visual Principles 터치 스와이프는 방향 잠금 로직을 사용합니다. 가로 의도가 확인되면 카드 스와이프, 세로 의도가 크면 페이지 스크롤을 유지합니다.
- Intro motion 터치 스크럽은 `233svh`, 최소 `1320px` 기준입니다. 더 빠르거나 느리게 조정할 때는 높이값을 바꾸는 방식으로 접근합니다.
- Hero 태블릿 구간 `max-width: 1200px`은 Figma `Hero_Tablet` 프레임을 기준으로 모바일처럼 독립 레이아웃으로 분기합니다. 좌측 정렬 축소형 규칙은 더 이상 사용하지 않습니다.
- Hero를 제외한 정보 섹션의 텍스트는 공통 타이포그래피 토큰 `title`, `body`, `state` 세 가지로 관리합니다. 새 섹션을 추가할 때도 먼저 이 세 속성 중 하나를 선택합니다.

제거했거나 제거할 수 있는 항목:

- 이전 `History/index_*.html` 스냅샷은 최신 스냅샷을 만들 때 삭제합니다.
- Visual Principles에서 현재 쓰는 자산은 `card-principles-graphic.svg`, `card-vision-grid.png`, `card-understood-visual.jpg`, `card-expressive-gaze-bg.png`, `card-future-form.png`입니다. 예전 백업이나 이전 카드 이미지는 보관하지 않습니다.
- 카드 폭을 위한 `calc(100vw - 160px)`, `calc(100vw - 72px)`, `calc(100vw - 48px)` 같은 개별 예외는 다시 추가하지 않습니다.

추가할 때 지킬 기준:

- 새 섹션은 Hero를 제외하면 기본 정보 영역 `--section-width` 기준에 맞춥니다.
- 새 카드/텍스트 섹션은 먼저 Figma 레이어 기준을 확인하고, 레이아웃 기준이 생기면 이 문서에 함께 기록합니다.
- 새 이미지/영상 자산은 `assets/images` 또는 `assets/media` 아래에 넣고, 파일 구조 목록에 사용 목적을 추가합니다.
- 현재 favicon은 브라우저 탭용 SVG data URL입니다. iOS 홈 화면 아이콘, PNG fallback, SNS 공유 이미지가 필요해지면 별도 파일 자산과 meta 태그를 추가합니다.

## Figma 기준

- Figma 파일명: `Labs Portfolio`
- Figma 파일 키: `4iXf45zdfYnJyxwyeDGC7e`
- 현재 확인한 page/canvas: `Rookie2`
- 주요 레이어 구조:
  - `Landing`
  - `Hero`
  - `Hero_Tablet`
  - `Hero_Mobile`
  - `Intro`
  - `Intro_mv`
  - `Intro_mv_end`
  - `Visual Principles`
  - `Interface Design` (현재 Figma 레이어명은 `Intro_mv`, 내부 텍스트 기준)
- Figma의 `Intro` node id는 `1:26`입니다.
- Figma의 `Hero_Tablet` node id는 `30:2`입니다.
- Figma의 `Hero_Mobile` node id는 `18:2`입니다.
- Figma의 `Visual Principles` node id는 `18:25`입니다.
- Figma의 `Interface Design` section node id는 `37:29`입니다.

Figma 디자인을 다시 반영할 때는 먼저 Figma에서 해당 node를 확인하고, `index.html`의 현재 수작업 구조에 맞게 CSS/HTML로 변환합니다.

## 전체 구조

현재 페이지는 다음 순서로 구성되어 있습니다.

1. `Hero`
2. `Intro`
3. `Intro_mv` scroll-scrub video
4. `Visual Principles` horizontal card carousel
5. `Interface Design`

`Hero`와 `Intro`는 `.hero-intro` 래퍼 안에 함께 들어 있습니다. 데스크톱/일반 포인터 환경에서는 Hero 배경을 별도 fixed 레이어로 두고, Hero 텍스트와 Intro 섹션이 스크롤 흐름 안에서 움직입니다. 터치 환경에서는 fixed 레이어 어긋남을 피하기 위해 Hero 배경도 문서 흐름과 함께 움직이게 합니다.

```html
<main class="landing">
  <div class="hero-intro">
    <div class="hero-intro__background">...</div>
    <section class="hero">...</section>
    <section class="intro">...</section>
  </div>
  <section class="intro-motion">...</section>
  <section class="section03 visual-principles">...</section>
  <section class="section04 interface-design">...</section>
</main>
```

## 공통 타이포그래피 기준

Hero는 이 기준에서 제외합니다. Hero 아래 정보 섹션의 텍스트 크기는 `index.html`의 `:root`에서 세 가지 토큰으로 관리합니다.

- `title`: 섹션의 큰 타이틀입니다. 예: `Moving What Matters`, `Visual Principles`, `Interface Design`
- `body`: 큰 타이틀 아래 설명문입니다. 예: Intro 서브 텍스트
- `state`: 중간 강조 텍스트입니다. 예: Intro motion overlay 카피, Visual Principles 카드 타이틀, Interface Design 아이콘 아래 카피

현재 반응형 크기 기준:

- 기본: `title 60px`, `body 24px`, `state 36px`
- 1600 이하: `title 51px`, `body 20px`, `state 31px`
- 1200 이하: `title 42px`, `body 18px`, `state 26px`
- 760 이하: `title 34px`, `body 16px`, `state 20px`

Visual Principles 1번 카드 안의 `Lively`, `Connected`, `Future` 라벨은 이미지 안에 얹는 예외 라벨이므로 이 공통 토큰을 따르지 않고 `--visual-label-size`로 별도 관리합니다.

## Hero 동작 기준

Hero 배경은 데스크톱/일반 포인터 환경에서 완전 고정이 아니라 약한 parallax로 움직입니다.

- 데스크톱/일반 포인터 환경에서 `.hero-intro__background`는 `position: fixed`입니다.
- 스크롤이 Hero 구간을 지나갈 때 배경은 Intro가 올라오는 거리의 약 30%만큼 위로 이동합니다.
- JS에서 `--hero-bg-offset` CSS 변수를 갱신합니다.
- 역스크롤하면 같은 비율로 원위치로 돌아옵니다.
- 터치 환경 `hover: none` + `pointer: coarse`에서는 iOS rubber-band/visual viewport와 fixed 레이어가 어긋나는 문제를 피하기 위해 `.hero-intro__background`를 `position: absolute`로 바꾸고 parallax transform을 끕니다. 이때 로봇 배경은 Hero/Intro 텍스트와 같은 문서 레이어로 움직입니다.

Hero 배경 레이어:

- 기본 이미지: `HeroImg.png`
- 컬러 효과 레이어: `HeroImg_Color.png`
- 컬러 레이어는 `hero-color-pulse` 애니메이션으로 동작합니다.
- 현재 pulse는 5초 반복입니다.
  - 0~2초: opacity 0
  - 2~3.5초: opacity 0 -> 0.7
  - 3.5~5초: opacity 0.7 -> 0
- Hero 중앙 하단에는 `Scroll` 안내와 세로 라인 애니메이션 `.hero-scroll`을 둡니다. 기본 `bottom: 40px`, 태블릿 `28px`, 모바일 `24px` 기준입니다.

Hero 반응형 기준:

- 기본: 1920 기준, 배경은 1920 이상 커지지 않음
- `max-width: 1600px`: Hero 텍스트/하단 요소 약 85% 스케일
- `max-width: 1200px`: 태블릿
  - Figma `Hero_Tablet` 프레임 기준: `1200 x 800`
  - 모바일과 같은 중앙형 구조로 분기합니다.
  - Hero 높이는 `clamp(600px, calc(31vw + 428px), 800px)`로 1200px에서는 800px에 맞춥니다.
  - 배경 미디어는 하단 고정, 1200px 기준 `1000 x 564`, `left: calc(50% - 18px)`
  - 기본 이미지 `object-fit: cover`, 컬러 레이어 `object-fit: contain`
  - 컬러 레이어의 `hero-color-pulse` 애니메이션은 데스크톱/태블릿/모바일 공통으로 유지
  - NAVER LABS 로고는 상단 중앙, `116 x 12`, `top: 40px`, 블랙
  - 타이틀은 상단 중앙, 최대 `80px`, `line-height: 0.7`, 1200px 기준 `top: 152px`, width `296px`
  - 설명 묶음은 1200px 기준 `top: 248px`, width `252px`, 중앙 정렬
  - 설명 eyebrow는 `20px`, body는 `16px`, body color `#818590`
  - 태블릿 body도 Figma처럼 3줄로 고정하기 위해 `.hero__body-line`을 block + `white-space: nowrap`으로 처리합니다.
- `max-width: 560px`: 모바일
  - Figma `Hero_Mobile` 프레임 기준: `390 x 600`
  - Hero 높이 `600px`
  - 배경 미디어는 하단 고정, `532 x 300`, `left: calc(50% - 5px)`
  - 기본 이미지 `object-fit: cover`, 컬러 레이어 `object-fit: contain`
  - 컬러 레이어의 `hero-color-pulse` 애니메이션은 데스크톱/태블릿/모바일 공통으로 유지
  - NAVER LABS 로고는 상단 중앙, `96 x 10`, `top: 40px`, 블랙
  - 타이틀은 상단 중앙, `68px`, `line-height: 0.705`, `top: 130px`, width `252px`
  - 설명 묶음은 `top: 218px`, width `252px`, 중앙 정렬
  - 타이틀과 설명 묶음의 세로 간격은 `40px`
  - 설명 eyebrow는 `20px`, body는 `16px`, body color `#818590`, eyebrow/body 간격은 `16px` 시각 기준에 맞춰 CSS margin `10px`
  - 모바일 body는 정보량을 줄이기 위해 2줄 전용 카피 `Scaling autonomous delivery / across real-world buildings.`를 사용합니다. 데스크톱/태블릿의 3줄 카피는 숨깁니다.

## Intro 현재 기준

현재 표시 문구:

- Title: `Moving What Matters`
- Body: `ROOKIE2 automates countless movements throughout modern buildings, allowing people to focus on what matters most. Designed to make even the smallest delivery feel seamless, efficient, and effortless.`

보관용 한글 문구는 `assets/content/intro.json`에 있습니다.

Intro 디자인 기준:

- 배경: `#09090b`
- 텍스트 컬러: Figma `Grayscale/Gray-100`, `#F9F9FA`
- 메인 타이틀:
  - `font-weight: 600`
  - 공통 `title` 토큰 사용
  - `line-height: var(--type-title-line)`
- 서브 텍스트:
  - `color: rgba(249, 249, 250, 0.9)`
  - 공통 `body` 토큰 사용
  - `line-height: var(--type-body-line)`

Intro 레이아웃 기준:

- `.intro__copy`는 하단 `bottom: 0`에 붙어 있습니다.
- 1600 이상에서는 Intro 상단 여백을 더 확보하기 위해 별도 높이 규칙을 사용합니다.
- 메인/서브 간격은 기본 `margin: clamp(18px, 1.667vw, 32px) auto 0`입니다.
- 모바일 제외, 561px 이상에서는 Figma 기준에 맞춰 `margin-top: clamp(28px, 2.083vw, 40px)`입니다.
- `.intro__copy`는 공통 정보 폭 `--section-width`를 사용하고, 서브 텍스트는 메인 타이틀보다 조금 넓은 정도로 제한합니다.
- `.intro__body` 최대 폭:
  - 기본: `760px`
  - 1600 이하: `720px`
  - 1200 이하: `512px`
  - 560 이하: `350px`

## Intro Motion 영상 기준

`Intro_mv.mp4`는 스크롤에 따라 재생/역재생됩니다.

- 섹션: `.intro-motion`
- 내부 stage: `.intro-motion__stage`
- 영상: `.intro-motion__video`
- 영상 overlay 카피: `.intro-motion__copy`
- `.intro-motion__stage`는 `position: sticky; top: 0; height: 100svh;`
- 영상은 `object-fit: cover`
- 현재 section 높이는 기본 `400svh`, 최소 `2080px`
- 1200 이하 비터치 환경에서는 `368svh`, 최소 `1840px`
- 560 이하 모바일과 1200 이하 터치 환경에서는 현재 기준보다 약 `1.5배` 빠른 스크럽을 위해 `233svh`, 최소 `1320px`
- 영상 뒤에는 Figma `Section03` 기준의 빈 섹션 `.section03`이 이어지며, 배경은 `#0d0b0b`입니다.

Intro motion overlay 카피 기준:

- Figma 레이어: `Intro_mv_end` 안의 `Txt`
- 문구: `Every delivery is a small movement. Together, they shape the rhythm of a building. Rookie2 is designed to keep that rhythm moving.`
- 위치는 모든 반응형 지점에서 공통 정보 영역 `--section-width`의 왼쪽 기준선과 맞춥니다. 1920 기준 `x: 360`, 1600 기준 `x: 200`, 1200 기준 `x: 40`, 모바일 390 기준 `x: 28`입니다.
- 최대 폭: `600px`
- 카피 폭은 데스크톱/태블릿에서 `min(600px, var(--section-width))`, 모바일에서는 `var(--section-width)`입니다.
- 폰트: Pretendard SemiBold, 공통 `state` 토큰, `line-height: var(--type-state-line)`, color `#f9f9fa`
- 영상 시간 기준 약 `1.6s`부터 등장하며, 기존 완료 시점은 유지하기 위해 약 `2.45s`에 제 위치에 도달합니다.
- 등장 동작은 스크롤 progress에 종속됩니다.
  - opacity: `0 -> 1`
  - translateY: `80px -> 0`
  - 역스크롤 시 동일 progress가 반대로 계산되어 `1 -> 0`, `0 -> 80px`로 되감깁니다.

동작 개념:

- 영상 섹션이 화면에 닿으면 stage가 viewport에 고정됩니다.
- 스크롤을 내리면 영상 시간이 앞으로 이동합니다.
- 역스크롤하면 영상 시간이 뒤로 이동합니다.
- overlay 카피는 영상 scrub 시간과 같은 상태값에 묶여 함께 등장/퇴장합니다.
- 영상 끝까지 도달하면 다음 섹션이 생겼을 때 다음 스크롤 흐름으로 넘어가게 됩니다.

주의:

- `html`, `body`의 `overflow-x`는 `clip`입니다.
- 이전에 `hidden`일 때 sticky가 풀리는 문제가 있었으므로, 특별한 이유 없이 `overflow-x: hidden`으로 되돌리지 않습니다.

## Visual Principles / Section03 기준

`Intro_mv` 이후의 다음 정보 섹션은 Figma `Visual Principles` 레이어를 기준으로 구현합니다.

- 섹션 클래스: `.section03.visual-principles`
- 배경: `#0d0b0b`
- Figma 기준 1920px 화면에서 title은 x `360`, y `240` 위치이며, 정보 섹션의 1200px inner 왼쪽에 맞춥니다.
- 타이틀: `Visual Principles`, Pretendard SemiBold, 공통 `title` 토큰, `line-height: var(--type-title-line)`
- 카드 기본 폭은 모든 반응형 지점에서 정보 영역과 같은 `--section-width`를 기준으로 합니다. 활성 카드의 좌측선은 항상 Visual Principles 타이틀 좌측선과 맞아야 합니다.
- 카드 기본 높이는 데스크톱 시작 기준 `675px`입니다.
- 반응형 breakpoint는 기본적으로 사이트 전체 기준인 `1600px`, `1200px`, `560px`를 따르되, `Visual Principles` 카드 캐러셀은 이미지/텍스트 충돌을 막기 위해 전용 `760px` 완충 구간을 사용합니다.
- 섹션 하단 여백은 데스크톱 기본 기준 `120px`입니다. 반응형 구간은 1600 이하 `58px`, 1200 이하 `56px`, 모바일 `48px` 기준입니다.
- 카드 간격: `28px`
- 카드 radius: `36px`
- 카드 배경:
  - 모든 카드 공통: `#19191a`
  - 3번 `Designed to Be Understood`: `#19191a` 기반 + 배경 이미지 `mix-blend-mode: screen`
  - 4번 `Expressive Gaze`: 배경 이미지 위에 흰색 선 5개를 CSS 요소로 얹고, 양끝 긴 선은 `xx.html`의 로봇 눈 깜빡임과 같은 `2.2s cubic-bezier(0.48, 0, 0.22, 1)` 타이밍을 사용합니다. 양끝 선은 Figma의 `strokeWeight 31px` + 세로 선분 `34px` 기준을 흉내 내며, blink 중간에는 선분 길이가 `1px`이 된 상태처럼 원형에 가깝게 줄어듭니다.
  - 5번: Figma 이미지 그대로 `object-fit: cover`로 표시합니다.
- 카드 트랙은 viewport 전체 폭 위에 놓고, 활성 카드의 중심이 항상 viewport 중심에 오도록 `transform`으로 이동합니다. 이 구조 덕분에 활성 카드의 좌우에 걸치는 이전/다음 카드의 노출 폭이 동일합니다.
- 화면이 줄어들면 카드 너비/높이와 공통 `state` 텍스트가 함께 단계적으로 줄어듭니다.
- 모바일 좌우 여백은 정보 영역 기준과 같은 `28px`입니다. 중심 카드 폭은 `var(--section-width)`를 사용해 Visual Principles 타이틀과 카드의 좌측 기준선을 맞춥니다.
- 모바일 `560px` 이하에서 5개 카드 공통 높이는 `320px`입니다.

카드 자산 관리 원칙:

- 카드 안의 비주얼은 카드별로 하나의 이미지 파일로 보관합니다.
- 카드 내부 텍스트는 이미지에 굽지 않고 HTML/CSS로 별도 구현합니다.
- 현재 카드 순서:
  - 1번: `Three Principles Behind Rookie2`
  - 2번: `Shaping the Vision`
  - 3번: `Designed to Be Understood`
  - 4번: `Expressive Gaze`
  - 5번: 이미지 카드
- 1번 카드의 세 가지 라벨 `Lively Interaction`, `Connected Experience`, `Approachable Future`도 CSS 텍스트로 얹습니다. 모바일 `560px` 이하에서는 각각 `Lively`, `Connected`, `Future`로 축약하고 `12px` 정수 크기를 사용합니다.
- 1번 카드의 동글한 컬러 그래픽은 PNG 캡처가 아니라 SVG 벡터를 사용합니다. 원본 `900 x 282` 비율을 유지해야 하며, `preserveAspectRatio="xMidYMid meet"`와 CSS `object-fit: contain` 기준을 사용합니다. 검은 사각 배경이 보이거나 모바일에서 찌그러져 보이면 SVG 비율 설정을 먼저 확인합니다.
- 1번 카드 내부 라벨 텍스트는 모바일에서도 최소 `10px` 이상을 유지합니다.
- 2번 카드의 이미지 그리드는 하나의 투명 PNG로 저장했습니다. 이미지 바깥 배경은 투명해야 하며, 검은 캔버스가 포함된 PNG로 교체하지 않습니다.
- 2번 카드는 모바일 `560px` 이하에서만 이미지 그리드를 카드 폭보다 크게 배치합니다. 비율을 유지한 채 좌우로 걸치게 하고, 넘치는 영역은 `.visual-card`의 `overflow: hidden`으로 마스킹합니다. 이때 타이틀과 이미지를 하나의 세로 그룹으로 보고 카드 상하 중앙에 배치합니다.
- 모바일 `560px` 이하의 2번 카드 이미지 그리드는 원본 크기감을 유지하되, 내부 `.visual-card__vision-mask`로 좌우 끝 열을 숨겨 가운데 3열 x 2줄, 총 6개 타일만 보이게 합니다.
- 3번 카드는 Figma 최신 기준에 따라 `Designed to Be Understood` 타이틀과 배경 비주얼만 표시합니다.
- 3번 카드 타이틀은 모든 반응형 지점에서 2번 카드 `Shaping the Vision` 타이틀의 상단 높이와 맞춥니다. 현재 구현은 2번 카드 이미지 영역과 같은 비율의 투명 스페이서를 사용해 두 카드의 타이틀 높이를 동일하게 유지합니다.
- 모바일 `560px` 이하의 3번 카드 배경 비주얼은 하단에 붙어 있어야 합니다. 타이틀과 이미지가 닿지 않도록 하단을 `-30px`로 걸치고, 이미지 폭은 `min(calc(121% + 106px), 520px)`로 제한합니다.
- 4번 카드의 흰색 선은 배경 이미지와 같은 `1200 x 768` 좌표계 안에 넣습니다. 카드 비율이 바뀌어 배경 이미지가 cover/crop 되더라도 선이 배경과 같은 비율과 위치로 움직여야 합니다. 양끝 긴 선은 전체 시각 높이 `65px` 기준에서 `32px`까지 줄어들도록 구현합니다. 이는 Figma의 세로 선분 길이 `34px -> 1px`에 stroke cap `31px`이 더해진 시각 크기입니다. 라운드 캡이 찌그러지지 않도록 `transform: scaleY()`가 아니라 pseudo-element의 `height`를 애니메이션합니다.
- 4번 카드 텍스트는 좌측 하단 정렬입니다. 좌측 간격은 반응형 inset 값을 사용하며, 데스크톱 시작 기준은 `100px`입니다. 하단 간격은 baseline 착시 보정을 위해 좌측 inset의 `90%`를 사용합니다.

캐러셀 동작:

- `.visual-principles__track`은 네이티브 가로 스크롤이 아니라 `transform: translate3d(...)` 기반으로 동작합니다. 브라우저 기본 scroll snap이 개입하면 드래그 후 순간 이동처럼 보일 수 있으므로 사용하지 않습니다.
- 마우스/터치 드래그가 가능하며, 드래그가 끝나면 requestAnimationFrame 기반 보간 애니메이션으로 부드럽게 스냅합니다.
- 드래그 스냅은 중앙 기준이 아니라 방향 기준입니다. 카드 간격의 약 `15%` 이상만 당겨도 드래그 방향의 다음/이전 카드로 넘어갑니다.
- 터치 환경에서는 방향 잠금 로직을 사용합니다. 손가락이 약 `8px` 이상 움직인 뒤 가로 이동이 세로 이동보다 충분히 크면 카드 스와이프로 잠그고, 세로 이동이 더 크면 페이지 스크롤을 유지합니다.
- 인디케이터는 JS에서 카드 개수를 읽어 자동 생성합니다. 카드가 4개 이상으로 늘어나도 `data-visual-card` article만 추가하면 인디케이터가 함께 늘어납니다.
- 인디케이터 hover는 조금 밝은 회색, active는 흰색 긴 pill 형태입니다.
- 기존 전역 커스텀 wheel/key 스크롤이 카드 가로 슬라이드를 방해하지 않도록 Visual Principles 영역은 예외 처리되어 있습니다.

## Interface Design / Section04 기준

`Visual Principles` 이후의 다음 섹션은 Figma의 `Interface Design` 레이어를 기준으로 구현합니다.

- 섹션 클래스: `.section04.interface-design`
- 배경: Figma 기준 `#100B0B`
- 현재 구현 기준 1920px 화면에서 inner는 x `360`, y `113` 위치이며, 정보 섹션의 1200px inner 왼쪽에 맞춥니다.
- 섹션은 Figma의 큰 블록 순서인 `ColorTypo` → `Icon` → `Info` 순서로 구성합니다. 1920px 기준 큰 블록 간격은 `240px`입니다.
- `Visual Principles` 인디케이터 하단에서 `Interface Design` 타이틀 상단까지의 Figma 기준 간격은 1920px에서 `373px`입니다. 현재 CSS에서는 `.section03` 하단 padding과 `.section04` 상단 padding의 합으로 맞춥니다.
- 타이틀: `Interface Design`, Pretendard SemiBold, 공통 `title` 토큰, `line-height: var(--type-title-line)`
- 타이틀 직하단에는 Figma 기준 body 문구를 사용합니다. `body` 토큰을 따르고, 타이틀과 본문 사이 간격은 1920px 기준 `40px`입니다.
- `ColorTypo` 영역은 컬러 팔레트, 타이포 샘플, 중앙 설명문으로 구성합니다.
  - 컬러 팔레트는 1200px inner 안에서 top row `586 + 586`, right split `279 + 279`, bottom row `381.333 * 3` 비율을 따릅니다.
  - 컬러 카드 radius는 1920px 기준 `36px`, gap은 `28px`입니다.
  - 모바일에서도 하단 Status Red/Yellow/Green 카드는 3열을 유지합니다. 모바일 컬러 카드는 모두 높이 `160px`, 내부 여백 `16px`로 맞추고, 컬러 라벨 전체를 더 작은 텍스트로 줄입니다.
  - 타이포 샘플은 `Aa` 3개를 Regular, Medium, SemiBold 기준으로 노출합니다.
  - 중앙 설명문은 공통 `state` 토큰을 따르고, 1920px 기준 폭 `800px`입니다.
- 아이콘 세트는 `assets/json`의 Lottie JSON을 사용합니다. 현재 Figma 노출 기준 15개를 사용하고, `Globe.json`은 Figma에서 hidden 상태라 제외합니다.
- Lottie 엔진은 외부 CDN에 의존하지 않고 `assets/js/lottie.min.js` 로컬 파일을 사용합니다. 회사망, 배포 환경, 오프라인 검수에서 아이콘이 빈 슬롯으로 보이는 문제를 피하기 위한 기준입니다.
- `file://`로 `index.html`을 직접 열어도 아이콘이 보이도록, 런타임은 JSON 파일을 직접 fetch하지 않습니다. `assets/js/interface-lottie-data.js`에 15개 JSON을 묶어 `window.ROOKIE2_INTERFACE_LOTTIES`로 제공하고, HTML의 `data-lottie-key`로 매칭합니다.
- 데스크톱 기준 아이콘 슬롯은 `160px`, 5열, column/row gap `100px`입니다. `1200px` inner 안에 정확히 맞도록 구성합니다.
- 아이콘은 버튼 슬롯 중앙에 Lottie를 렌더링합니다. 슬롯과 Lottie 스케일을 분리해 나중에 아이콘 크기 조절이 쉽도록 합니다.
- 아이콘 hover/tap 확대는 grid layout에 영향을 주면 안 됩니다. `.interface-icon` 슬롯은 고정 크기/고정 좌표를 유지하고, `.interface-icon__motion`은 `position: absolute`로 중앙 배치해 `width/height`가 변해도 행간과 위치가 밀리지 않게 합니다.
- hover 또는 터치 tap 시 해당 Lottie가 재생되고, 활성 아이콘은 기본 `160px` 슬롯 기준 `138%` 크기처럼 보입니다.
- 모바일 `560px` 이하에서는 hover/tap 확대 크기는 유지하고, 기본 상태의 내부 Lottie 크기만 현재 모바일 기준에서 10% 줄입니다. 슬롯 크기와 그리드 위치는 유지합니다.
- hover 종료, blur, 다른 아이콘 선택 시 즉시 끊지 않고 현재 루프가 끝나는 지점까지 재생한 뒤 각 아이콘의 시작/정지 프레임으로 돌아가 정지합니다. 기본값은 `0`프레임입니다.
- 개별 아이콘은 `data-lottie-start-frame`과 CSS 크기/위치 클래스로 예외 값을 줄 수 있습니다. 현재 4번째 `Congrat` 아이콘은 시작/정지 프레임 `20`, 기본 크기 `83%`, 활성 크기 `114%`를 사용합니다. `Sports`와 `Siren`은 내부 Lottie 위치만 보정합니다. 종료 시에는 종료 요청 시점과 관계없이 현재 루프를 끝까지 재생한 뒤, 다음 루프의 `0`프레임대부터 지정 시작 프레임까지 자연스럽게 지나간 뒤 정지합니다.
- 아이콘 아래 카피는 Figma 기준 문구 `A library of over 80 icons helps communicate status, intent, and emotion through a clear and expressive visual language.`를 사용하며, 공통 `state` 토큰을 따릅니다.
- `Info` 영역은 `Visual Principles` 캐러셀과 같은 스와이프/인디케이터 감각을 사용하지만, 단위는 개별 카드가 아니라 `1200px 그룹`입니다.
  - 1번 그룹: 1200px 안에 `586 + 586` 두 카드
    - 두 카드는 Figma에서 추출한 `assets/images/interface-design/info-card-01-left.png`, `assets/images/interface-design/info-card-01-right.png`를 사용합니다.
  - 2번 그룹: 1200px 단일 카드
  - 3번 그룹: 1200px 안에 `400 + 772` 비율의 두 카드
  - 4번 그룹: 1200px 단일 카드
  - 현재 카드들은 비어 있는 placeholder로 유지하고, 추후 콘텐츠/이미지를 채웁니다.
  - 카드와 인디케이터 사이 간격은 `Visual Principles`와 동일하게 맞춥니다. 현재 기준은 데스크톱 `40px`, 1200px 이하 `34px`, 760px 이하 및 모바일 `28px`입니다.
- 반응형 breakpoint는 사이트 기본 기준인 `1600px`, `1200px`, `560px`를 따릅니다.
- 모바일 `560px` 이하에서는 아이콘을 3열로 배치해 터치 타깃과 가독성을 확보합니다.
- 모바일 `560px` 이하에서는 `Visual Principles`와의 경계에서 흰 배경이 1px 새지 않도록 `.section04`에 `margin-top: -1px` 보정을 둡니다.
- 모바일 `560px` 이하에서는 데스크톱 좁은 창에서 과한 빈 공간이 생기지 않도록 `.section03`의 `min-height: 100svh`를 `auto`로 풉니다.

## 스크롤/비디오 스크립트 기준

스크립트는 `index.html` 하단에 있습니다.

주요 함수:

- `updateHeroBackground()`: Hero 배경 parallax offset 갱신
- `getMotionProgress()`: Intro motion 섹션 내 스크롤 progress 계산
- `updateVideoTarget()`: progress를 video target time으로 변환
- `scrub()`: 영상 currentTime을 targetTime으로 부드럽게 따라가게 함. 터치 환경에서는 더 빠르게 따라붙도록 보간값을 높입니다.
- `scrollToPosition()`: wheel/key 커스텀 스크롤 처리

현재 wheel/key 이벤트는 `preventDefault()`를 사용해 직접 scroll position을 제어합니다. 반면 모바일/태블릿 터치는 브라우저의 네이티브 관성 스크롤을 유지하고 `touchmove`를 가로채지 않습니다. 첫 `touchstart`에서는 영상 프라임을 수행합니다.

## 콘텐츠/언어 기준

- 한글 줄바꿈은 반드시 띄어쓰기 구간에서 줄바꿈되도록 유지합니다.
- 현재 `body`에 아래 규칙이 적용되어 있습니다.

```css
word-break: keep-all;
overflow-wrap: normal;
```

- 특별히 요청받지 않는 한 `Rookie2`처럼 자연스러운 표기를 기본으로 합니다.
- 전체 대문자 표기는 앞으로 거의 사용하지 않는 방향입니다. 단, 현재 Intro 영문 body에는 사용자가 준 원문 그대로 `ROOKIE2`가 들어가 있습니다. 사용자가 다시 지시하면 `Rookie2`로 바꿉니다.

## 앞으로 추가될 정보 섹션 기준

Hero는 이 기준에서 제외합니다. 사용자가 별도로 제외할 섹션을 말하지 않으면, Hero 아래의 정보/콘텐츠 섹션은 기본적으로 다음 폭 기준을 사용합니다.

- 기본 정보 섹션 최대 폭: `1200px`
- 텍스트 중심 섹션: 필요 시 `960px` 권장
- 긴 본문 문단: 필요 시 `720~820px` 권장
- 카드 그리드: 필요 시 `1200~1280px` 권장

권장 전역 변수:

```css
:root {
  --section-max: 1200px;
  --section-side: 80px;
  --section-gutter: 160px;
  --section-width: min(calc(100vw - var(--section-gutter)), var(--section-max));
}
```

권장 inner 패턴:

```css
.section__inner {
  width: min(calc(100% - (var(--section-side) * 2)), var(--section-max));
  margin: 0 auto;
}
```

반응형 좌우 여백 기준:

- 데스크톱: `80px`
- 1600 이하: `64px`
- 1200 이하: `40px`
- 모바일: `28px`

현재 `Intro`와 `Visual Principles`는 모두 `--section-width`를 기준으로 정보 영역의 좌우 기준선을 맞춥니다. 텍스트 자체는 필요하면 더 좁은 `max-width`를 가질 수 있지만, 섹션의 기준 컨테이너는 동일해야 합니다.

나중에 전체 정보 영역을 `960px` 등으로 바꾸고 싶을 경우, 섹션마다 직접 값을 바꾸지 말고 전역 변수만 바꿀 수 있는 구조로 작업합니다.

## 작업 시 주의사항

- 기존 visual/scroll 감각을 깨지 않도록 Hero, Intro, Intro motion은 서로 레이어와 스크롤 타이밍이 연결되어 있음을 기억합니다.
- Hero 배경은 데스크톱/일반 포인터에서 fixed + JS parallax입니다. 터치 환경에서는 iOS 레이어 어긋남 방지를 위해 absolute로 전환합니다. 단순 sticky로 바꾸면 이전처럼 의도대로 동작하지 않을 수 있습니다.
- Intro motion은 sticky 영상 구조입니다. `overflow-x: clip`을 유지합니다.
- 신규 섹션을 추가할 때는 영상 이후에 붙이는 것이 기본입니다.
- 새로운 텍스트/카드 섹션을 만들 때는 위의 `1200px` 정보 섹션 기준을 우선 적용합니다.
- 사용자가 Figma를 업데이트했다고 말하면 Figma node를 다시 확인하고 반영합니다.
- 중요한 디자인 기준, 예외, 콘텐츠 결정이 생기면 이 문서를 함께 업데이트합니다.
