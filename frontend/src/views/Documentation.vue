<script setup>
  import PageTitle from "../components/PageTitle.vue"
  import Button from "../components/Button.vue"
</script>

<template>
  <PageTitle>Documentation</PageTitle>
  <div class="hero">
    <div class="hero-title">Invoice</div>
    <div class="hero-content">
      A web application designed to simplify the process
      of creating and managing invoices for businesses and individuals.
    </div>
    <Button
      @click="$router.push('/')"
      class="hero-button"
      bg="secondary">
        Try now
    </Button>
    <div class="menu">
      <a class="page-link" href="#core-features"><div class="menu-item">
        <div class="menu-icon">
          <span class="material-symbols-outlined">star</span>
        </div>
        <div class="menu-text">Core features</div>
      </div></a>
      <a class="page-link" href="#how-to-use"><div class="menu-item">
        <div class="menu-icon">
          <span class="material-symbols-outlined">book</span>
        </div>
        <div class="menu-text">How to use</div>
      </div></a>
      <a class="page-link" href="#how-it-works"><div class="menu-item">
        <div class="menu-icon">
          <span class="material-symbols-outlined">schema</span>
        </div>
        <div class="menu-text">How it works</div>
        </div></a>
      <a class="page-link" href="#and-more"><div class="menu-item">
        <div class="menu-icon">
          <span class="material-symbols-outlined">more_horiz</span>
        </div>
        <div class="menu-text">And more</div>
        </div></a>
    </div>
  </div>
  <section id="core-features">
    <div class="section-header">Core features</div>
    <div class="section-content">
      <div class="feat">
        <div class="feat-title">Intuitive UI</div>
        <div class="feat-content">
          It features a clean and straightforward user interface
          designed for ease  of use. Whether you are a business
          owner or an individual, the  intuitive layout ensures
          that you can quickly navigate through the app,  create
          invoices effortlessly without any hassle. The minimalistic
          design  reduces clutter and focuses on providing a seamless
          user experience,  making it accessible even for those who
          are not tech-savvy.
        </div>
      </div>
      <div class="feat">
        <div class="feat-title">Optimized for Mobile</div>
        <div class="feat-content">
          It is fully optimized for mobile devices, allowing you to
          manage your  invoicing tasks on the go. The responsive
          design ensures that all  features and functionalities are
          easily accessible and user-friendly on  smartphones and
          tablets. Whenever you need to create an invoice, you can
          do it from your mobile device with the same efficiency as
          on a desktop.  This mobile optimization ensures you stay
          productive and in control of  your billing, no matter
          where you are.
        </div>
      </div>
      <div class="feat">
        <div class="feat-title">Unique Invoice Number</div>
        <div class="feat-content">
          This web app automatically generates a unique invoice
          number for each  new invoice, ensuring complete accuracy
          and organization in your billing  process. This feature
          helps prevent duplication and makes it easy to  track and
          reference individual invoices. With a unique identifier
          for  every invoice, managing your financial records becomes
          more  straightforward and efficient, reducing the risk of
          errors and improving  overall accountability.
        </div>
      </div>
    </div>
  </section>
  <section id="how-to-use">
    <div class="section-header">How to use</div>
    <div class="step">
      <div class="s-content">
        <div class="step-title">Step 1</div>
        <div class="step-content">
          <span class="step-sub-title">Create an invoice.</span>
          <br>
          Click the "Create invoice" button on the Home page.
          This will take you to the Create Invoice page.
        </div>
      </div>
      <div class="step-image">
        <img src="https://ik.imagekit.io/prezzgh/invoice/home.png?updatedAt=1718329877014" alt="homepage image">
      </div>
    </div>
    <div class="step rev">
      <div class="s-content">
        <div class="step-title">Step 2</div>
        <div class="step-content">
          <span class="step-sub-title">Fill out the form.</span>
          <br>
          On the Create Invoice page, complete the form to generate
          your invoice. When you're done, click the "Create" button
          at the bottom of the page.
        </div>
      </div>
      <div class="step-image">
        <img src="https://ik.imagekit.io/prezzgh/invoice/form.png?updatedAt=1718329876854" alt="create invoice page">
      </div>
    </div>
    <div class="congrats">
      <div class="huge">That's it!</div>
      <div>You have just created an invoice.</div>
    </div>
  </section>
  <section id="how-it-works">
    <div class="section-header">How it works</div>
    <div class="section-content">
      <div class="function">
        <div class="function-title">
          <span class="material-symbols-outlined">storage</span>
          <div class="title-content">Storage</div>
        </div>
        <div class="function-content">
          Our web app uses the JavaScript localStorage API to store data
          on your browser, allowing partial offline use and eliminating
          the need to log in for each session. You'll need to allow the
          browser to store data on your device. Note that this data can
          be cleared by you or the browser at any time, so we recommend
          logging in to save your data to our servers for consistent access.
        </div>
      </div>
      <div class="function">
        <div class="function-title">
          <span class="material-symbols-outlined">security</span>
          <div class="title-content">Security</div>
        </div>
        <div class="function-content">
          We prioritize your privacy and security. We do not request,
          process, or store any personal data on our servers. Instead,
          we use Auth0, a trusted third-party service, to manage
          authentication and authorization for our users. This approach
          ensures that your personal information is handled securely and
          efficiently. By leveraging Auth0, we provide robust security
          measures without compromising your privacy.
        </div>
      </div>
    </div>
  </section>
  <section id="and-more">
    <div class="section-header">And more</div>
    <div class="section-content">
      <div class="more">
        <div class="more-icon">
          <span class="material-symbols-outlined">code</span>
        </div>
        <div class="more-title">CONTRIBUTE</div>
        <div class="more-content">
          This project is open source, and the source code is available
          on <a href="https://github.com/10thcode/invoice">GitHub</a>.
          We welcome your ideas and contributions.
        </div>
      </div>
      <div class="more">
        <div class="more-icon">
          <span class="material-symbols-outlined">bug_report</span>
        </div>
        <div class="more-title">REPORT AN ISSUE</div>
        <div class="more-content">
          If you encounter any issues, you can either contact the developer
          directly or open an issue on
          <a href="https://github.com/10thcode/invoice">GitHub</a>.
        </div>
      </div>
      <div class="more">
        <div class="more-icon">
          <span class="material-symbols-outlined">face_6</span>
        </div>
        <div class="more-title">ABOUT THE DEV</div>
        <div class="more-content">
          Learn more about the developer who created this web application
          by visiting their portfolio at
          <a href="https://10thcode.me"> 10thcode.me</a>.
        </div>
      </div>
    </div>
  </section>
</template>

<style scoped>

  .function-title {
    display: flex;
    align-items: center;
    gap: 16px;
  }

  .step-sub-title {
    font-weight: 400;
  }

  .step-image {
    text-align: center;
  }

  img {
    max-width: 260px;
    height: auto;
  }

  section {
    margin-bottom: 32px;
  }

  .feat, .step, .function, .more {
    display: flex;
    flex-direction: column;
    gap: 32px;
    padding: 32px;
  }

  .feat-title, .step-title, .function-title {
    font-size: 32px;
  }

  .more-title {
    font-size: 14px;
    font-weight: 700;
    letter-spacing: 8px;
  }
  
  .more-icon span {
    font-size: 48px;
  }

  .feat-content, .step-content, .function-content, .more-content { 
    line-height: 33px;
    font-size: 20px;
    font-weight: 300;

  }

  .section-header {
    background: var(--secondary);
    padding: 32px;
    text-align: center;
    font-size: 24px;
    font-weight: 300;
  }
  .hero {
    background: url('https://ik.imagekit.io/prezzgh/invoice/hero_background.jpg?updatedAt=1717805134229');
    background-repeat: no-repeat;
    background-size: cover;
    display: flex;
    flex-direction: column;
    justify-content: center;
    gap: 32px;
    padding: 0 32px;
    height: 100vh;
  }

  .menu {
    color: white;
    display: flex;
    flex-direction: column;
    gap: 16px;
  }

  .page-link {
    color: white;
  }

  .menu-item {
    display: flex;
    gap: 16px;
    align-items: center;
  }

  .hero-title, .hero-content {
    color: white;
  }

  .hero-title {
    font-size: 48px;
  }

  .hero-content {
    font-size: 20px;
    font-weight: 300;
    line-height: 33px;
  }

  .hero-button {
    width: 102px;
  }

  .s-content {
    display: flex;
    flex-direction: column;
    gap: 32px;
  }

  .congrats {
    font-size: 20px;
    font-weight: 300;
    text-align: center;
    padding: 32px 0;
  }

  .huge {
    font-size: 64px;
  }

  @media (min-width: 768px) {
    .hero {
      align-items: center;
      padding: 0 64px;
      
    }

    .hero-title {
      font-size: 64px;
    }

    .hero-content {
      text-align: center;
      max-width: 500px;
      font-size: 24px;
    }

    .menu {
      flex-direction: row;
      gap: 32px;
    }

    .section-content {
      padding: 0 64px;
    }

    .step {
      flex-direction: row;
      justify-content: center;
      align-items: center;
    }

    .rev {
      flex-direction: row-reverse;
    }

    
    .step > div {
      width: 40%;
    }
  }

  @media (min-width: 1024px) {
    .step > div {
      width: 30%;
    }

    .section-content {
      display: flex;
      justify-content: center;
    }

    .feat, .function {
      width: 30%;
    }
  }
</style>
