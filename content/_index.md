---
# Leave the homepage title empty to use the site title
title: ''
summary: ''
date: 2026-08-27
type: landing

sections:
  - block: resume-biography-3
    content:
      # Choose a user profile to display (a folder name within `content/authors/`)
      username: me
      text: ''
      # Show a call-to-action button under your biography? (optional)
      # button:
      #   text: Download CV
      #   url: uploads/resume.pdf
      headings:
        about: ''
        education: ''
        interests: ''
    design:
      # Use the new Gradient Mesh which automatically adapts to the selected theme colors
      background:
        gradient_mesh:
          enable: true

      # Name heading sizing to accommodate long or short names
      name:
        size: md # Options: xs, sm, md, lg (default), xl

      # Avatar customization
      avatar:
        size: medium # Options: small (150px), medium (200px, default), large (320px), xl (400px), xxl (500px)
        shape: circle # Options: circle (default), square, rounded
  - block: markdown
    content:
      title: '🔬 Research'
      subtitle: ''
      text: |-
        Our group works at the intersection of **quantum optics, near-field nano-imaging, and low-temperature precision measurement**:

        - **Quantum imaging** — entangled-photon microscopy and super-resolution imaging beyond the classical limit, including quantum microscopy of biological cells at the Heisenberg limit.
        - **Near-field scanning imaging** — tip-enhanced Raman spectroscopy and imaging (TERS) with single-molecule and single-base resolution, from DNA/RNA sequencing to 2D materials and live cells.
        - **Low-temperature precision measurement** — nanofilm optomechanical thermometry and heat-transport physics at cryogenic temperatures for quantum devices.

        We are always looking for motivated students and collaborators — feel free to reach out! 😃
    design:
      columns: '1'
  - block: collection
    id: papers
    content:
      title: Featured Publications
      filters:
        folders:
          - publications
        featured_only: true
    design:
      view: article-grid
      columns: 2
  - block: collection
    content:
      title: Recent Publications
      text: ''
      filters:
        folders:
          - publications
        exclude_featured: false
    design:
      view: citation
---
