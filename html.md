# Content Models | Sololearn 

"NOTES"  Clipped from: https://www.sololearn.com/

- Metadata: Content that sets up the presentation or behavior of the rest of the content. These elements are found in the head of the document.

- Elements: `<base>`, `<link>`, `<meta>`, `<noscript>`, `<script>`, `<style>`, `<title>`

- Embedded: Content that imports other resources into the document.

- Elements: `<audio>`, `<video>`, `<canvas>`, `<iframe>`, `<img>`, `<math>`, `<object>`, `<svg>`

- Interactive: Content specifically intended for user interaction.

- Elements: `<a>`, `<audio>`, `<video>`, `<button>`, `<details>`, `<embed>`, `<iframe>`, `<img>`, `<input>`, `<label>`, `<object>`, `<select>`,
  `<textarea>`

- Heading: Defines a section header.

- Elements: `<h1>`, `<h2>`, `<h3>`, `<h4>`, `<h5>`, `<h6>`, `<hgroup>`

- Phrasing: This model has a number of inline level elements in common with HTML4.

- Elements: `<img>`, `<span>`, `<strong>`, `<label>`, `<br/>`, `<small>`, `<sub>`, and more.
- The same element can belong to more than one content model.
- Flow content: Contains the majority of HTML5 elements that would be included in the normal flow of the document.

- Sectioning content: Defines the scope of headings, content, navigation, and footers.   Elements: `<article>`, `<aside>`, `<nav>`, `<section>`

* The various content models overlap in certain areas, depending on how they are being used.

## `<header></header>` 

- In HTML4, we would define a header like this:

  `<div id="header"> `

- In HTML5, a simple `<header>` tag is used, instead.
- The `<header>` element is appropriate for use inside the body tag.

## `<footer></footer>`

- The footer element is also widely used. Generally we refer to a section located at the very bottom of the web page as the footer.
- The following information is usually provided between these tags:
  - Contact Information
  - Privacy Policy
  - Social Media Icons
  - Terms of Service
  - Sitemap. a list of a websites pages. It is  usually used for others to easily organize your websites pages. Googles current algorithm also looks
    at your sitemap for search indexing.

## `<nav></nav>`

- This tag represents a section of a page that links to other pages or to certain sections within the page. This would be a section with navigation
  links.   - Here is an example of a major block of navigation links:

  ```
  <nav>
    <ul>
      <li>
        <a href="#">Home</a>
      </li>
      <li>
        <a href="#">Services</a>
      </li>
      <li>
        <a href="#">About us</a>
      </li>
    </ul>
  </nav>
  ```

- Anchored `<a></a>` links allow the user to jump to a different section of the same document.
- Not all of the links in a document should be inside a `<nav>` element.
- The `<nav>` element is intended only for major blocks of navigation links.
- Typically, the `<footer>` element often has a list of links that don't need to be in a `<nav>` element.

## `<article></article>`

- Article is a self-contained, independent piece of content that can be used and distributed separately from the rest of the page or site.
- This could be a forum post, a magazine or newspaper article, a blog entry, a comment, an interactive widget or gadget, or any other independent
  piece of content.   - The `<article>` element replaces the `<div>` element that was widely used in HTML4, along with an id or class.

      ```
      <article> 
          <h1>The article title</h1> 
          <p>Contents of the article element </p> 
      </article> 
      ```

- When an `<article>` element is nested, the inner element represents an article related to the outer element. For example, blog post comments can be
  `<article>` elements nested in the `<article>` representing the blog post.

## `<section></section>` 

- `<section>` is a logical container of the page or article.
- Sections can be used to divide up content within an article.
- For example, a homepage could have a section for introducing the company, another for news items, and still another for contact information.
- For example: News (section) Something new (article) Another new (article) About company (section) History (article) What we do (article) Comments
  (section) 1st comment (article) 2nd comment (article) ... IT is up to you, you decide, what is section (logical part) and what is article (content)
- Each `<section>` should be identified, typically by including a heading (h1-h6 element) as a child of the `<section>` element.

  ```
  <article> 
  <h1>Welcome</h1> 
      <section> 
          <h1>Heading</h1> 
          <p>content or image</p> 
      </section> 
  </article>
  ```

- If it makes sense to separately syndicate the content of a `<section>` element, use an `<article>` element instead.

## `<aside></aside>` 

- `<aside>` is secondary or tangential content which could be considered separate from but indirectly related to the main content.
- This type of content is often represented in sidebars.  When an `<aside>` tag is used within an `<article>` tag, the content of the `<aside>` should
  be specifically related to that article.

  ```
  <article>
    <h1> Gifts for everyone </h1>
    <p> This website will be the best place for choosing gifts </p>
    <aside>
      <p>Gifts will be delivered to you within 24 hours </p>
    </aside>
  </article>
  ```

- When an `<aside>` tag is used outside of an `<article>` tag, its content should be related to the surrounding content.

## `Progress Bar` 

- The `<progress>` element provides the ability to create progress bars on the web.
- The progress element can be used within headings, paragraphs, or anywhere else in the body.
- Progress Element Attributes  Value: Specifies how much of the task has been completed.  Max: Specifies how much work the task requires in total.

Example:  `<progress min="0" max="100" value="35"> </progress>`

- Use the `<progress>` tag in conjunction with JavaScript to dynamically display a task's progress.

## `Web Storage `

- With HTML5 web storage, websites can store data on a user's local computer.
- Before HTML5, we had to use JavaScript cookies to achieve this functionality.
- The Advantages of Web Storage
  - More secure
  - Faster
  - Stores a larger amount of data
  - Stored data is not sent with every server request
- Local storage is per domain. All pages from one domain can store and access the same data.

## `Types of Web Storage Objects` 

- There are two types of web storage objects:

  - sessionStorage()
  - localStorage()

- Local vs. Session
  - Session Storage is destroyed once the user closes the browser
  - Local Storage stores data with no expiration date
- You need to be familiar with basic JavaScript in order to understand and use the API.

## `Responsive Web Design` 

- Responsive web design is the practice of building websites that can adapt to every device and every screen size.
- A responsive website is usable on different screen sizes, from large desktops to small mobile screens.
- The main concept of responsive web design is building layouts that respond to screen size change by adapting and changing the style of the page.
- Example:

      Let's take a look at the project we will build: a generic Landing Page for an app.

  This is how it will look like on a desktop:

- As you can see, the landing page has a number of sections:

  - a header with texts and a button
  - a features section
  - a quote section
  - a footer with a menu

- A landing page is where users land when clicking on promotional/marketing links. For example, when you want to promote your app, you share its
  landing page URL on social and other media.

## `Viewport `

- `viewport`: the visible area of a web page.  Usually, a web page with a fixed width becomes too large to fit the viewport on a small screen, such as
  a mobile device or tablet. To fix this, browsers on those devices scaled down the entire web page to fit the screen.

- You can control the viewport of your web pages.

- You can control your viewport in HTML5 using a meta tag:

  ```
  <meta name="viewport" content="width=device-width,initial-scale=1.0"> 
  ```

- **_width=device-width_** sets the width of the page to follow the screen-width of the device.  initial-scale=1.0 sets the initial zoom level when
  the page is first loaded by the browser.

- You can also use custom values for the viewport tag, however in most cases it is recommended you use the defaults by applying
  the device-width value.

## `Media-query `

- Media queries provide the ability to specify different CSS styles for different widths of the viewport, or other specifications.  This makes it
  possible for a web page to define different layout styles for different screen sizes and make the page responsive!

- You define a media query using the @media rule inside of your existing style sheet:

  ```
  @media screen and (max-width: 600px) { 
    body { 
      background-color: blue; 
    } 
  }
  ```

- The @media rule is followed by the media type we are targeting (the screen in our case) and sets the condition when the rules apply
  (max-width:600px in our case).
- So now, the style will apply if the page has a width up to 600px.
- You can also define multiple conditions, for example a max and min width of the viewport:

  ```
  @media screen and (min-width: 800px) and (max-width: 1024px) { 
    body { 
      background-color: blue; 
    } 
  }
  ```

- Now the style will apply for screen sizes from 800 to 1024px.

- You can also define multiple media queries for a single web page.
- Media queries allow you to define breakpoints when the page layout and style should change, as well as define the corresponding CSS styles for these
  breakpoints.
- Here are some of the most common practices to follow when building a responsive web page:

  - Use relative units (such as percentages) for the sizes of the elements and fonts.

  - Use CSS media queries to define breakpoints and layout changes.
  - Define the viewport to adapt to mobile screens.
  - Use CSS Flexbox to make it easier to create flexible layouts.
