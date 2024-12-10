import http from 'k6/http'
import { check, sleep } from 'k6'
import { htmlReport } from 'https://raw.githubusercontent.com/benc-uk/k6-reporter/main/dist/bundle.js'

const k6VUS = __ENV.K6_VUS
const k6DURATION = __ENV.K6_DURATION
const type = __ENV.TYPE

export default function() {
  const url = 'http://localhost:8000/asking'

  const question = 'How are you?'

  const payload = JSON.stringify({
    question: question,
  })

  const params = {
    headers: {
      'Content-Type': 'application/json',
    },
  }

  const res = http.post(url, payload, params)

  check(res, {
    'is status 200': (r) => r.status === 200,
  })

  sleep(1)
}

export function handleSummary(data) {
  return {
    [`reports/${type}/result-${k6DURATION}-${k6VUS}.json`]: JSON.stringify(data, null, 2),
    [`reports/${type}/result-${k6DURATION}-${k6VUS}.html`]: htmlReport(data),
  }
}
