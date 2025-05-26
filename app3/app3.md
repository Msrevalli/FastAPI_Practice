### 1. `/header-example/`

**Request Header**:

```
User-Agent: Mozilla/5.0
```

**Response**:

```json
{
  "User-Agent": "Mozilla/5.0"
}
```

---

### 2. `/custom-header/`

**Request Header**:

```
X-Token: abc123
```

**Response**:

```json
{
  "X-Token": "abc123"
}
```

---

### 3. `/optional-header/`

**No header provided**

**Response**:

```json
{
  "X-Lang": "en"
}
```

**With Header**:

```
X-Lang: fr
```

**Response**:

```json
{
  "X-Lang": "fr"
}
```

---

### 4. `/multi-header/`

**Request Header**:

```
X-Tags: tag1, tag2
```

**Response**:

```json
{
  "X-Tags": ["tag1", "tag2"]
}
```

---

### 5. `/mixed-headers/`

**Request Headers**:

```
X-Token: secure456
X-Lang: de
```

**Response**:

```json
{
  "X-Token": "secure456",
  "X-Lang": "de"
}
```

---

### 6. `/secure-data/`

✅ **Correct Token**:

```
X-Token: secure123
```

**Response**:

```json
{
  "data": "Secret information"
}
```

❌ **Incorrect Token**:

```
X-Token: wrongtoken
```

**Response**:

```json
{
  "detail": "Invalid token"
}
```

---

### 7. `/inspect/`

**Request Headers**:

```
User-Agent: PostmanRuntime/7.32.2
Accept-Language: en-US,en;q=0.9
```

**Response**:

```json
{
  "User-Agent": "PostmanRuntime/7.32.2",
  "Accept-Language": "en-US,en;q=0.9"
}
```

---

### 8. `/feature-flag/`

**Header**:

```
X-Debug: true
```

**Response**:

```json
{
  "debug_mode": true
}
```

**Without Header**:

```json
{
  "debug_mode": false
}
```

---

### 9. `/version/`

**Header**:

```
X-API-Version: v2
```

**Response**:

```json
{
  "API-Version": "v2"
}
```

**Without Header**:

```json
{
  "API-Version": "v1"
}
```

---


