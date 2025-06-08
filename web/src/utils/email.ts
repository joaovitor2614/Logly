

export function getMaskedEmail(email: string) {
    const [localPart, emailDomain] = email.split('@');
    if (localPart.length <= 2) {
        return '*'.repeat(localPart.length) + '@' + emailDomain;
    }

    const visibleChars = 2;
    const maskedPart = '*'.repeat(localPart.length - visibleChars);

    return localPart.slice(0, visibleChars) + maskedPart + '@' + emailDomain
}