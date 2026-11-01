---
layout: post
title: "DAST·SAST·SCA 톺아보기 [Week 1]"
date: 2026-09-27 18:32:20 +09:00
categories: ["Let's Pay1oad/🐣Team.GAST"]
tags: ["dast","sast","SCA"]
permalink: "/entry/DAST-톺아보기-Week-1/"
legacy_url: "https://spactcodes.tistory.com/entry/DAST-%ED%86%BA%EC%95%84%EB%B3%B4%EA%B8%B0-Week-1"
image: "/assets/images/posts/cover-9a6e5129a66d61cbf8cc3588.png"
---

{% raw %}
#### <strong># DAST란?</strong>

동적 애플리케이션 보안 테스트(Dynamic Application Security Testing)는 소스 코드를 보지 않고, 애플리케이션이 실제 실행 중인 상태(Runtime)에서 외부 해커의 시선으로 취약점을 찾아내는 블랙박스(Black-Box) 보안 테스트 기법이다. 본 기법은 애플리케이션의 보안 무결성을 검증하고 잠재적 위협에 대한 대응력을 극대화하기 위해, 공격 표면(Attack Surface) 탐색부터 취약점 악용 시뮬레이션에 이르는 4단계의 체계적인 기술 프로세스를 기반으로 작동한다.

<strong>1. 정찰 : 헤드리스 브라우저(Headless Browser)와 동적 크롤링</strong>

최근의 웹(React, Vue 등)은 화면을 동적으로 그려낸다. 최신 DAST는 화면이 없는 가상 브라우저(Headless Browser)를 띄워 DOM(문서 객체 모델)을 직접 렌더링 하고 자바스크립트를 실행해 숨겨진 API 엔드포인트(서버가 클라이언트의 요청을 수신하고 자원에 접근할 수 있도록 허용하는 디지털 위치이자 특정 URL 주소)까지 찾아낸다.

<figure class="imagegridblock"><div class="image-container"><span data-url="/assets/images/posts/40b32c1ccf3bf77b04160593b4e3177a4ad01819.png" data-phocus="/assets/images/posts/40b32c1ccf3bf77b04160593b4e3177a4ad01819.png" data-is-animation="false" data-origin-width="623" data-origin-height="623" data-filename="DAST_1.png" style="width: 39.5349%; margin-right: 10px;" data-widthpercent="40"><img src="/assets/images/posts/40b32c1ccf3bf77b04160593b4e3177a4ad01819.png" loading="lazy" width="623" height="623"></span><span data-url="/assets/images/posts/bc4d0b42d0b9653e7198dc79d9b2c4e103fc0a0b.png" data-phocus="/assets/images/posts/bc4d0b42d0b9653e7198dc79d9b2c4e103fc0a0b.png" data-origin-width="768" data-origin-height="512" data-filename="01_headless_browser_dynamic_crawling.png" data-is-animation="false" style="width: 59.3023%;" data-widthpercent="60"><img src="/assets/images/posts/bc4d0b42d0b9653e7198dc79d9b2c4e103fc0a0b.png" loading="lazy" width="768" height="512"></span></div></figure>

<strong>2. 타격 시뮬레이션 : 퍼징(Fuzzing)과 페이로드(Payload) 주입</strong>

맵핑된 진입점에 퍼징(Fuzzing) 기법을 사용해 무작위 또는 자동 변이된 악성 데이터(페이로드)를 입력 폼, HTTP 헤더, 쿠키 등에 초당 수백 번씩 주입한다.

<figure class="imagegridblock"><div class="image-container"><span data-url="/assets/images/posts/0e4c7c15bea387776591f39116dab6afbbad4fc4.png" data-phocus="/assets/images/posts/0e4c7c15bea387776591f39116dab6afbbad4fc4.png" data-is-animation="false" data-origin-width="623" data-origin-height="623" data-filename="DAST_2.png" style="width: 39.5349%; margin-right: 10px;" data-widthpercent="40"><img src="/assets/images/posts/0e4c7c15bea387776591f39116dab6afbbad4fc4.png" loading="lazy" width="623" height="623"></span><span data-url="/assets/images/posts/d1a94ca36332a9debe5d06a316105d6e044cd9cb.png" data-phocus="/assets/images/posts/d1a94ca36332a9debe5d06a316105d6e044cd9cb.png" data-origin-width="768" data-origin-height="512" data-filename="02_fuzzing_payload_injection.png" data-is-animation="false" style="width: 59.3023%;" data-widthpercent="60"><img src="/assets/images/posts/d1a94ca36332a9debe5d06a316105d6e044cd9cb.png" loading="lazy" width="768" height="512"></span></div></figure>

<strong>3. 블라인드 취약점 탐지: OAST(Out-of-Band AST)</strong>

보안이 꽤 적용된 서버는 공격을 받아도 에러 창을 띄우지 않는  '블라인드(Blind)' 상태를 유지한다. 이를 파훼하기 위해 DAST는 외부 리스너 서버(OAST : 클라이언트나 다른 프로그램으로부터의 네트워크 연결 요청을 받아들이고 대기(Listen)하며, 이를 적절한 데이터베이스 인스턴스나 서비스로 연결해 주는 역할을 하는 컴포넌트 또는 서버)를 띄우고, 타겟 서버가 스스로 외부로 통신(DNS/HTTP 등)을 보내도록 유도하는 특수 페이로드를 던진다.

<figure class="imagegridblock"><div class="image-container"><span data-url="/assets/images/posts/97e27c8040b0780c8c8eb81420c7c9af47ed58a5.png" data-phocus="/assets/images/posts/97e27c8040b0780c8c8eb81420c7c9af47ed58a5.png" data-is-animation="false" data-origin-width="623" data-origin-height="623" data-filename="DAST_3.png" style="width: 39.5349%; margin-right: 10px;" data-widthpercent="40"><img src="/assets/images/posts/97e27c8040b0780c8c8eb81420c7c9af47ed58a5.png" loading="lazy" width="623" height="623"></span><span data-url="/assets/images/posts/e7aa227194c27efb1a24534f75b1b73ad948973c.png" data-phocus="/assets/images/posts/e7aa227194c27efb1a24534f75b1b73ad948973c.png" data-origin-width="768" data-origin-height="512" data-filename="03_oast_blind_vulnerability_detection.png" data-is-animation="false" style="width: 59.3023%;" data-widthpercent="60"><img src="/assets/images/posts/e7aa227194c27efb1a24534f75b1b73ad948973c.png" loading="lazy" width="768" height="512"></span></div></figure>

<strong>4. 논리적 약점 공략 : 상태 기반 테스트(State-based Testing)</strong>

애플리케이션의 로그인 인증(Authentication) 및 세션(Session) 상태를 유지하면서, 권한 우회(Privilege Escalation)나 여러 프로세스가 동시에 접근할 때 꼬이는 현상인 경쟁 상태(Race Condition)를 테스트한다.

<figure class="imagegridblock"><div class="image-container"><span data-url="/assets/images/posts/e7f8cd300f21f1ea2b80af78b604348ce6b1bb9b.png" data-phocus="/assets/images/posts/e7f8cd300f21f1ea2b80af78b604348ce6b1bb9b.png" data-is-animation="false" data-origin-width="623" data-origin-height="623" data-filename="DAST_4.png" style="width: 39.5349%; margin-right: 10px;" data-widthpercent="40"><img src="/assets/images/posts/e7f8cd300f21f1ea2b80af78b604348ce6b1bb9b.png" loading="lazy" width="623" height="623"></span><span data-url="/assets/images/posts/ba09585220e25050a8acb959d4374cb343ba2d3f.png" data-phocus="/assets/images/posts/ba09585220e25050a8acb959d4374cb343ba2d3f.png" data-origin-width="768" data-origin-height="512" data-filename="04_state_based_testing.png" data-is-animation="false" style="width: 59.3023%;" data-widthpercent="60"><img src="/assets/images/posts/ba09585220e25050a8acb959d4374cb343ba2d3f.png" loading="lazy" width="768" height="512"></span></div></figure>

#### <strong># DAST의 실무적 가치</strong>

> <strong>&nbsp;강점</strong>
{: data-ke-style="style2"}

<strong>1. <span><b>런타임 환경 취약점 발견</b>:</span></strong> 소스 코드를 정적으로 분석해서는 절대 찾을 수 없는 서버 설정 오류, 잘못된 세션 및 인증 처리 결함 등을 잡아내는 데 탁월하다.

<strong>2. <span>낮은 오탐률(False Positive):</span></strong> 코드상의 이론적인 결함이 아니라, 실제로 외부에서 접근 및 익스플로잇(Exploit) 가능한 취약점만 식별하므로 경고의 신뢰도가 높다.

<strong>3. 언어 및 환경 독립성:</strong> 코드를 보지 않기 때문에 내부에서 어떤 프로그래밍 언어를 썼는지 무관하게 작동하며, 외부 벤더가 제공한 서드파티(Third-party) 모듈을 검증할 때도 유용하다.

> <strong>한계</strong>
{: data-ke-style="style2"}

<strong>1. <span>근본 원인 파악의 어려움:</span></strong> 소스 코드에 대한 가시성이 없으므로, 취약점을 발견하더라도 개발자에게 문제의 '정확한 코드 라인'을 짚어주지 못한다.

<strong>2. <span>느린 스캔 속도 및 높은 수정 비용:</span></strong> 애플리케이션 전체를 크롤링하므로 스캔에 수 시간에서 며칠이 소요될 수 있다. 또한, SDLC(소프트웨어 개발 생명주기) 후반부에 취약점이 발견되기 때문에 이를 수정하는 데 드는 시간과 비용이 상대적으로 크다.

#### <strong># SAST란?</strong>

정적 애플리케이션 보안 테스트 (SAST, Static Application Security Testing)\*\*는 애플리케이션을 실행하지 않은 상태에서 소스 코드, 바이트코드 또는 바이너리를 직접 분석하여 보안 취약점을 식별하는 화이트박스(White-Box) 보안 테스트 기법이다. 본 기법은 소프트웨어 개발 생명주기(SDLC)의 초기 단계(코딩 및 빌드)에 보안 검증을 통합하는 시프트 레프트(Shift-Left) 전략의 핵심 도구로, 컴파일 또는 배포 전에 코드 내재적 결함을 수학적·논리적으로 찾아내는 기술 프로세스로 작동한다.

<strong>1. 구문 분석 및 추상 구문 트리(AST) 생성</strong>

소스 코드를 읽어 들여 프로그램의 문법적 구조를 계층적인 트리 형태(Abstract Syntax Tree)로 변환한다. 이를 통해 코드가 실행되는 논리적 구조를 수학적으로 모델링하여 깊이 있는 분석의 기반을 마련한다.

<figure class="imageblock alignCenter" data-ke-mobilestyle="widthOrigin" data-filename="01_ast_parsing_1536x1024.png" data-origin-width="1536" data-origin-height="1024"><span data-url="/assets/images/posts/8c8568f314f68d0dc9966e6b29ed0c1936707148.png" data-phocus="/assets/images/posts/8c8568f314f68d0dc9966e6b29ed0c1936707148.png"><img src="/assets/images/posts/8c8568f314f68d0dc9966e6b29ed0c1936707148.png" loading="lazy" width="1536" height="1024" data-filename="01_ast_parsing_1536x1024.png" data-origin-width="1536" data-origin-height="1024"></span></figure>

<strong>2. 오염 분석(Taint Analysis) 및 데이터 흐름 분석</strong>

외부로부터 입력된 신뢰할 수 없는 데이터(Source)가 애플리케이션 내부 변수와 함수를 거쳐 어떻게 이동하는지 추적한다. 이 '오염된' 데이터가 적절한 필터링이나 검증 없이 데이터베이스 쿼리문이나 시스템 명령어 등 위험한 목적지(Sink)에 도달하는 경로를 증명하여, SQL 인젝션(SQLi)이나 크로스 사이트 스크립팅(XSS) 취약점을 원천 탐지한다.

<figure class="imageblock alignCenter" data-ke-mobilestyle="widthOrigin" data-filename="02_taint_data_flow_1536x1024.png" data-origin-width="1536" data-origin-height="1024"><span data-url="/assets/images/posts/089b7d4e6c7b5ad5ae2af272d937f23c5ffb2af4.png" data-phocus="/assets/images/posts/089b7d4e6c7b5ad5ae2af272d937f23c5ffb2af4.png"><img src="/assets/images/posts/089b7d4e6c7b5ad5ae2af272d937f23c5ffb2af4.png" loading="lazy" width="1536" height="1024" data-filename="02_taint_data_flow_1536x1024.png" data-origin-width="1536" data-origin-height="1024"></span></figure>

<strong>3. 제어 흐름 분석(Control Flow Analysis)</strong>

프로그램이 실행될 수 있는 모든 논리적 분기(If, Switch 등)와 반복 루프 경로를 탐색한다. 실행 흐름상의 논리적 오류로 인해 발생할 수 있는 메모리 누수, 접근 통제 누락, 무한 루프, 버퍼 오버플로우 등의 취약 경로를 식별한다.

<figure class="imageblock alignCenter" data-ke-mobilestyle="widthOrigin" data-filename="03_control_flow_analysis_1536x1024.png" data-origin-width="1536" data-origin-height="1024"><span data-url="/assets/images/posts/acd6c7fc14c5ca079a818af7ebcf3430339fb3ad.png" data-phocus="/assets/images/posts/acd6c7fc14c5ca079a818af7ebcf3430339fb3ad.png"><img src="/assets/images/posts/acd6c7fc14c5ca079a818af7ebcf3430339fb3ad.png" loading="lazy" width="1536" height="1024" data-filename="03_control_flow_analysis_1536x1024.png" data-origin-width="1536" data-origin-height="1024"></span></figure>

<strong>4. 시맨틱 패턴 매칭(Semantic Pattern Matching)</strong>

구축된 보안 정책 및 알려진 취약점 데이터베이스를 바탕으로, 안전하지 않은 코딩 관행과 코드를 대조한다. 하드코딩된 암호화 키, 취약한 암호화 알고리즘(예: MD5, DES) 사용, 난수 생성기 결함 등 문맥적 보안 위반 사항을 찾아낸다.

<figure class="imageblock alignCenter" data-ke-mobilestyle="widthOrigin" data-filename="04_semantic_pattern_matching_1536x1024.png" data-origin-width="1536" data-origin-height="1024"><span data-url="/assets/images/posts/e9c53b1b2332a4a707eb8aa3013048ee8d3f38a7.png" data-phocus="/assets/images/posts/e9c53b1b2332a4a707eb8aa3013048ee8d3f38a7.png"><img src="/assets/images/posts/e9c53b1b2332a4a707eb8aa3013048ee8d3f38a7.png" loading="lazy" width="1536" height="1024" data-filename="04_semantic_pattern_matching_1536x1024.png" data-origin-width="1536" data-origin-height="1024"></span></figure>

#### <strong># </strong> <strong>SAST</strong><strong>의 실무적 가치</strong>

> 강점
{: data-ke-style="style2"}

<strong>1. 근본 원인 식별:</strong> 취약점이 존재하는 정확한 파일명과 소스 코드 라인 번호를 제시하여 개발자의 즉각적인 디버깅을 지원한다.

<strong>2. 초기 대응 비용 절감: </strong> 런타임 환경 구성이 필요 없으며, 개발 극초기에 문제를 발견하고 수정하므로 후반부 결함 수정에 비해 시간과 비용이 기하급수적으로 절감된다.

> 한계
{: data-ke-style="style2"}

<strong>1. 높은 오탐률(False Positive):</strong> 실제 운영 서버의 방어 기제(WAF 등)나 런타임 통제 환경을 고려하지 않고 코드만 분석하므로, 실제로는 익스플로잇이 불가능한 항목까지 취약점으로 과다 보고하는 경향이 있다.

<strong>2. 동적 결함 탐지 불가:</strong> 소스 코드로 드러나지 않는 서버 인프라 설정 오류, 세션 가로채기, 비정상적인 권한 우회 등의 런타임 취약점은 탐지할 수 없다.

#### <strong># SCA란?</strong>

소프트웨어 구성 분석 (SCA, Software Composition Analysis)은 애플리케이션 개발에 사용된 오픈소스 소프트웨어(OSS)와 서드파티(Third-party) 라이브러리를 식별하여, 알려진 보안 취약점과 라이선스 컴플라이언스(법적 준수) 문제를 탐지하는 자동화된 보안 테스트 기법이다. 현대의 소프트웨어는 밑바닥부터 작성되기보다 수많은 오픈소스 패키지를 조립하여 만들어진다. SCA는 개발자가 직접 작성한 코드(SAST 영역)가 아닌, 외부에서 가져온 부품들의 안전성을 검증하여 소프트웨어 공급망(Supply Chain)의 무결성을 확보하는 핵심 기술 프로세스로 작동한다.

<strong>1. 의존성 식별 및 명세서(SBOM) 생성</strong>

프로젝트 내의 패키지 관리자(npm, pip, Maven 등) 파일이나 빌드 결과물을 스캔하여, 사용된 모든 오픈소스 컴포넌트의 이름과 버전 정보를 추출한다. 이를 바탕으로 소프트웨어 자재 명세서인 SBOM(Software Bill of Materials)을 생성하여 애플리케이션의 구성 요소를 투명하게 목록화한다.

<strong>2. 전이적 의존성(Transitive Dependency) 추적</strong>

개발자가 직접 설치한 라이브러리(직접 의존성)뿐만 아니라, 그 라이브러리가 내부적으로 다시 불러와 사용하는 다른 라이브러리(간접/전이적 의존성)까지 깊이 있게 추적한다. 실제 보안 사고의 상당수는 개발자가 인지하지 못한 깊은 단계의 전이적 의존성 취약점에서 발생하기 때문에 이 과정은 매우 중요하다.

<strong>3. 취약점 데이터베이스(CVE/NVD) 대조</strong>

추출된 컴포넌트 및 버전 목록을 국가 취약점 데이터베이스(NVD)나 공통 취약점 및 노출(CVE) 사전, 그리고 보안 업체의 위협 인텔리전스와 실시간으로 대조한다. 이를 통해 특정 라이브러리의 현재 버전에 '이미 알려진(Known)' 해킹 결함이 존재하는지 수학적으로 판별한다.

<strong>4. 라이선스 호환성 및 법적 리스크 검증</strong>

오픈소스는 무료이지만 저마다 고유한 법적 사용 조건(라이선스)을 가진다. SCA는 기업의 상용 소프트웨어 소스 코드를 강제로 공개하게 만들 수 있는 전염성 라이선스(예: GPL, AGPL 등)가 포함되어 있는지 스캔하여 법률적, 지적 재산권 침해 리스크를 사전에 차단한다.

#### <strong># </strong> <strong>SCA </strong> <strong>의 실무적 가치</strong>

> 강점
{: data-ke-style="style2"}

<strong>1. 신속한 취약점 패치:</strong> 문제가 되는 정확한 라이브러리와 안전한 업데이트 버전을 즉각적으로 제시하여 빠른 조치가 가능하다.

<strong>2. 법적/컴플라이언스 리스크 완화:</strong> 보안 취약점뿐만 아니라 오픈소스 라이선스 위반에 따른 법적 분쟁 가능성을 사전에 통제한다.

> 한계
{: data-ke-style="style2"}

<strong>1. 제로데이(Zero-day) 탐지 불가:</strong> 이미 데이터베이스에 등록된 '알려진 취약점'만 찾아낼 수 있으므로, 아직 세상에 공개되지 않은 신규 취약점이나 개발자가 직접 짠 코드 내부의 결함은 탐지할 수 없다.

<strong>2. 도달 가능성(Reachability)의 한계:</strong> 애플리케이션이 취약한 라이브러리를 포함하고 있더라도, 실제 코드에서 그 취약한 '특정 함수'를 호출하지 않는다면 실질적인 위협이 되지 않음에도 이를 취약점으로 과다 보고할 수 있다.
{% endraw %}
