async function createAlgoliaInstance() {
  return await fetch(`${window.location.origin}/get_algolia_credentials/`)
    .then(async (response) => await response.json())
    .then((data) => algoliasearch(data.APP_ID, data.API_KEY));
}

createAlgoliaInstance().then((algoliaClient) => {
  const searchClient = {
    search(requests) {
      const hits = document.querySelector(".search-container");
      if (requests.every(({ params }) => !params.query)) {
        hits.style.display = "none";
        return Promise.resolve({
          results: requests.map(() => ({
            hits: [],
            nbHits: 0,
            nbPages: 0,
            page: 0,
            processingTimeMS: 0,
            hitsPerPage: 0,
            exhaustiveNbHits: false,
            query: "",
            params: "",
          })),
        });
      }
      hits.style.display = "block";
      return algoliaClient.search(requests);
    },
  };

  const productsIndex = "vishitiyshop_products";

  const search = instantsearch({
    indexName: productsIndex,
    searchClient,
  });

  search.addWidgets([
    instantsearch.widgets.searchBox({
      container: "#searchbox",
      placeholder: "Введiть запит...",
    }),
    instantsearch.widgets.configure({
      hitsPerPage: 10,
    }),
    instantsearch.widgets.hits({
      container: ".search-results",
      templates: {
        item: (hit, { html, components }) => html
        `
        <div class="card">
          <img src="${hit.image_url}" class="card-img-top" alt="${hit.title}" />
          <div class="card-body">
              <h5 class="card-title tetx-white">
                <a href="${hit.url}">${components.Highlight({ hit, attribute: 'title' })}</a>
              </h5>
              <h5 class="card-title" id="vis">vishitiy.ua</h5>
              <div class="card-footer text-white text-lg">
               Цiна: ${hit.price} UAH
              </div>
          </div>
        </div>
        `,
      },
    }),
    instantsearch.widgets.refinementList({
      container: `#type-refinement`,
      attribute: "type",
    }),
    instantsearch.widgets.refinementList({
      container: `#color-refinement`,
      attribute: "status",
    }),
  ]);
  search.start();
});
