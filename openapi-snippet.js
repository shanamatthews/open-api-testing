const OpenAPISnippet = require('openapi-snippet')

// define input:
const openApi = require('./openapi-derefed.json') // Open API document
const targets = ['node_unirest', 'c'] // array of targets for code snippets. See list below...

try {
  // either, get snippets for ALL endpoints:
  const results = OpenAPISnippet.getSnippets(openApi, targets) // results is now array of snippets, see "Output" below.


  // ...or, get snippets for a single endpoint:
//   const results2 = OpenAPISnippet.getEndpointSnippets(openApi, '/organizations/{organization_slug}/events', 'get', targets)

  console.log(results);
} catch (err) {
    console.log("err: " + err);

}