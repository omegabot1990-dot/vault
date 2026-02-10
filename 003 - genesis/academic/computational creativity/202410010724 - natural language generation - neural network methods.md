---
tags:
  - academic
  - cc
aliases:
  - computational creativity - lecture three
title: natural language generation - neural network methods
description: computational creativity - natural language generation - neural network methods - annotated
parent nodes:
  - "[[computational creativity]]"
child nodes: 
annotation-target: computational_creativity_03c_natural_language_generation_neural_network_methods.pdf
---




>%%
>```annotation-json
>{"created":"2024-10-01T14:41:26.781Z","text":"How does natural language generation with neural networks work?","updated":"2024-10-01T14:41:26.781Z","document":{"title":"03c Natural Language Generation Neural Network Methods","link":[{"href":"urn:x-pdf:d040e757a00f8c6dd8f715d9980d68cb"},{"href":"vault:/500 - attachments/computational_creativity_03c_natural_language_generation_neural_network_methods.pdf"}],"documentFingerprint":"d040e757a00f8c6dd8f715d9980d68cb"},"uri":"vault:/500 - attachments/computational_creativity_03c_natural_language_generation_neural_network_methods.pdf","target":[{"source":"vault:/500 - attachments/computational_creativity_03c_natural_language_generation_neural_network_methods.pdf","selector":[{"type":"TextPositionSelector","start":515,"end":542},{"type":"TextQuoteSelector","exact":"Natural Language Generation","prefix":" UniversityNeural Network Models","suffix":" The process of NLG with neural "}]}]}
>```
>%%
>*%%PREFIX%%UniversityNeural Network Models%%HIGHLIGHT%% ==Natural Language Generation== %%POSTFIX%%The process of NLG with neural*
>%%LINK%%[[#^8m4n7j854el|show annotation]]
>%%COMMENT%%
>How does natural language generation with neural networks work?
>%%TAGS%%
>#question
^8m4n7j854el


>%%
>```annotation-json
>{"created":"2024-10-01T14:42:01.454Z","updated":"2024-10-01T14:42:01.454Z","document":{"title":"03c Natural Language Generation Neural Network Methods","link":[{"href":"urn:x-pdf:d040e757a00f8c6dd8f715d9980d68cb"},{"href":"vault:/500 - attachments/computational_creativity_03c_natural_language_generation_neural_network_methods.pdf"}],"documentFingerprint":"d040e757a00f8c6dd8f715d9980d68cb"},"uri":"vault:/500 - attachments/computational_creativity_03c_natural_language_generation_neural_network_methods.pdf","target":[{"source":"vault:/500 - attachments/computational_creativity_03c_natural_language_generation_neural_network_methods.pdf","selector":[{"type":"TextPositionSelector","start":543,"end":765},{"type":"TextQuoteSelector","exact":"The process of NLG with neural networks is similar to NLG with Markov Chains: 1. Prepare a language dataset, e.g., tokenisation, stemming, embedding, etc. 2. Build a model using the dataset 3. Use a primer to generate text","prefix":"delsNatural Language Generation ","suffix":"Discover the world at Leiden Uni"}]}]}
>```
>%%
>*%%PREFIX%%delsNatural Language Generation%%HIGHLIGHT%% ==The process of NLG with neural networks is similar to NLG with Markov Chains: 1. Prepare a language dataset, e.g., tokenisation, stemming, embedding, etc. 2. Build a model using the dataset 3. Use a primer to generate text== %%POSTFIX%%Discover the world at Leiden Uni*
>%%LINK%%[[#^nj3kf871b8|show annotation]]
>%%COMMENT%%
>
>%%TAGS%%
>
^nj3kf871b8


>%%
>```annotation-json
>{"created":"2024-10-01T14:44:41.826Z","updated":"2024-10-01T14:44:41.826Z","document":{"title":"03c Natural Language Generation Neural Network Methods","link":[{"href":"urn:x-pdf:d040e757a00f8c6dd8f715d9980d68cb"},{"href":"vault:/500 - attachments/computational_creativity_03c_natural_language_generation_neural_network_methods.pdf"}],"documentFingerprint":"d040e757a00f8c6dd8f715d9980d68cb"},"uri":"vault:/500 - attachments/computational_creativity_03c_natural_language_generation_neural_network_methods.pdf","target":[{"source":"vault:/500 - attachments/computational_creativity_03c_natural_language_generation_neural_network_methods.pdf","selector":[{"type":"TextPositionSelector","start":845,"end":922},{"type":"TextQuoteSelector","exact":"Word embedding is typically the first step in transforming words into inputs ","prefix":" Layer vs Pre-trained Embeddings","suffix":"i.e. each word is represented as"}]}]}
>```
>%%
>*%%PREFIX%%Layer vs Pre-trained Embeddings%%HIGHLIGHT%% ==Word embedding is typically the first step in transforming words into inputs== %%POSTFIX%%i.e. each word is represented as*
>%%LINK%%[[#^c9ke7xn133|show annotation]]
>%%COMMENT%%
>
>%%TAGS%%
>
^c9ke7xn133


>%%
>```annotation-json
>{"created":"2024-10-01T14:45:21.867Z","updated":"2024-10-01T14:45:21.867Z","document":{"title":"03c Natural Language Generation Neural Network Methods","link":[{"href":"urn:x-pdf:d040e757a00f8c6dd8f715d9980d68cb"},{"href":"vault:/500 - attachments/computational_creativity_03c_natural_language_generation_neural_network_methods.pdf"}],"documentFingerprint":"d040e757a00f8c6dd8f715d9980d68cb"},"uri":"vault:/500 - attachments/computational_creativity_03c_natural_language_generation_neural_network_methods.pdf","target":[{"source":"vault:/500 - attachments/computational_creativity_03c_natural_language_generation_neural_network_methods.pdf","selector":[{"type":"TextPositionSelector","start":985,"end":1077},{"type":"TextQuoteSelector","exact":"It is possible to learn the embeddings for words as part of the training of a neural network","prefix":"s a word vector to the network  ","suffix":" i.e. use error gradients to adj"}]}]}
>```
>%%
>*%%PREFIX%%s a word vector to the network%%HIGHLIGHT%% ==It is possible to learn the embeddings for words as part of the training of a neural network== %%POSTFIX%%i.e. use error gradients to adj*
>%%LINK%%[[#^ic2fxpmc7b|show annotation]]
>%%COMMENT%%
>
>%%TAGS%%
>
^ic2fxpmc7b


>%%
>```annotation-json
>{"created":"2024-10-01T14:47:15.859Z","updated":"2024-10-01T14:47:15.859Z","document":{"title":"03c Natural Language Generation Neural Network Methods","link":[{"href":"urn:x-pdf:d040e757a00f8c6dd8f715d9980d68cb"},{"href":"vault:/500 - attachments/computational_creativity_03c_natural_language_generation_neural_network_methods.pdf"}],"documentFingerprint":"d040e757a00f8c6dd8f715d9980d68cb"},"uri":"vault:/500 - attachments/computational_creativity_03c_natural_language_generation_neural_network_methods.pdf","target":[{"source":"vault:/500 - attachments/computational_creativity_03c_natural_language_generation_neural_network_methods.pdf","selector":[{"type":"TextPositionSelector","start":1198,"end":1349},{"type":"TextQuoteSelector","exact":"Learning embeddings as part of the training can provide benefits because word use is specific to the task, and vectors are adjusted to promote learning","prefix":"mbedding layer for this purpose ","suffix":" Learning word embeddings is typ"}]}]}
>```
>%%
>*%%PREFIX%%mbedding layer for this purpose%%HIGHLIGHT%% ==Learning embeddings as part of the training can provide benefits because word use is specific to the task, and vectors are adjusted to promote learning== %%POSTFIX%%Learning word embeddings is typ*
>%%LINK%%[[#^ioi9c7l2ea|show annotation]]
>%%COMMENT%%
>
>%%TAGS%%
>
^ioi9c7l2ea


>%%
>```annotation-json
>{"created":"2024-10-01T14:47:38.331Z","updated":"2024-10-01T14:47:38.331Z","document":{"title":"03c Natural Language Generation Neural Network Methods","link":[{"href":"urn:x-pdf:d040e757a00f8c6dd8f715d9980d68cb"},{"href":"vault:/500 - attachments/computational_creativity_03c_natural_language_generation_neural_network_methods.pdf"}],"documentFingerprint":"d040e757a00f8c6dd8f715d9980d68cb"},"uri":"vault:/500 - attachments/computational_creativity_03c_natural_language_generation_neural_network_methods.pdf","target":[{"source":"vault:/500 - attachments/computational_creativity_03c_natural_language_generation_neural_network_methods.pdf","selector":[{"type":"TextPositionSelector","start":1470,"end":1623},{"type":"TextQuoteSelector","exact":"But for small corpuses of text, it may be more beneficial to use a pre-trained embedding to bring in knowledge about the general use of words in the text","prefix":"gnificantly impact the training ","suffix":"Discover the world at Leiden Uni"}]}]}
>```
>%%
>*%%PREFIX%%gnificantly impact the training%%HIGHLIGHT%% ==But for small corpuses of text, it may be more beneficial to use a pre-trained embedding to bring in knowledge about the general use of words in the text== %%POSTFIX%%Discover the world at Leiden Uni*
>%%LINK%%[[#^qjnveji1e7|show annotation]]
>%%COMMENT%%
>
>%%TAGS%%
>
^qjnveji1e7


>%%
>```annotation-json
>{"created":"2024-10-01T14:48:56.791Z","text":"What are recurrent neural network models?","updated":"2024-10-01T14:48:56.791Z","document":{"title":"03c Natural Language Generation Neural Network Methods","link":[{"href":"urn:x-pdf:d040e757a00f8c6dd8f715d9980d68cb"},{"href":"vault:/500 - attachments/computational_creativity_03c_natural_language_generation_neural_network_methods.pdf"}],"documentFingerprint":"d040e757a00f8c6dd8f715d9980d68cb"},"uri":"vault:/500 - attachments/computational_creativity_03c_natural_language_generation_neural_network_methods.pdf","target":[{"source":"vault:/500 - attachments/computational_creativity_03c_natural_language_generation_neural_network_methods.pdf","selector":[{"type":"TextPositionSelector","start":1765,"end":1803},{"type":"TextQuoteSelector","exact":"Recurrent Neural Networks (RNN) Models","prefix":"r the world at Leiden University","suffix":"Recurrent Neural Networks (RNN) "}]}]}
>```
>%%
>*%%PREFIX%%r the world at Leiden University%%HIGHLIGHT%% ==Recurrent Neural Networks (RNN) Models== %%POSTFIX%%Recurrent Neural Networks (RNN)*
>%%LINK%%[[#^3ie7rcmhxwj|show annotation]]
>%%COMMENT%%
>What are recurrent neural network models?
>%%TAGS%%
>#question
^3ie7rcmhxwj


>%%
>```annotation-json
>{"created":"2024-10-01T14:49:40.474Z","updated":"2024-10-01T14:49:40.474Z","document":{"title":"03c Natural Language Generation Neural Network Methods","link":[{"href":"urn:x-pdf:d040e757a00f8c6dd8f715d9980d68cb"},{"href":"vault:/500 - attachments/computational_creativity_03c_natural_language_generation_neural_network_methods.pdf"}],"documentFingerprint":"d040e757a00f8c6dd8f715d9980d68cb"},"uri":"vault:/500 - attachments/computational_creativity_03c_natural_language_generation_neural_network_methods.pdf","target":[{"source":"vault:/500 - attachments/computational_creativity_03c_natural_language_generation_neural_network_methods.pdf","selector":[{"type":"TextPositionSelector","start":1803,"end":1993},{"type":"TextQuoteSelector","exact":"Recurrent Neural Networks (RNN) RNNs take an input (e.g. a sentence) broken down into items (e.g. n-grams), produces output (e.g. next word) and an input to the next iteration (e.g. a model)","prefix":"ent Neural Networks (RNN) Models","suffix":" RNNs only capture backward depe"}]}]}
>```
>%%
>*%%PREFIX%%ent Neural Networks (RNN) Models%%HIGHLIGHT%% ==Recurrent Neural Networks (RNN) RNNs take an input (e.g. a sentence) broken down into items (e.g. n-grams), produces output (e.g. next word) and an input to the next iteration (e.g. a model)== %%POSTFIX%%RNNs only capture backward depe*
>%%LINK%%[[#^ggq8dhpqyxu|show annotation]]
>%%COMMENT%%
>
>%%TAGS%%
>
^ggq8dhpqyxu


>%%
>```annotation-json
>{"created":"2024-10-01T14:50:23.094Z","updated":"2024-10-01T14:50:23.094Z","document":{"title":"03c Natural Language Generation Neural Network Methods","link":[{"href":"urn:x-pdf:d040e757a00f8c6dd8f715d9980d68cb"},{"href":"vault:/500 - attachments/computational_creativity_03c_natural_language_generation_neural_network_methods.pdf"}],"documentFingerprint":"d040e757a00f8c6dd8f715d9980d68cb"},"uri":"vault:/500 - attachments/computational_creativity_03c_natural_language_generation_neural_network_methods.pdf","target":[{"source":"vault:/500 - attachments/computational_creativity_03c_natural_language_generation_neural_network_methods.pdf","selector":[{"type":"TextPositionSelector","start":1994,"end":2033},{"type":"TextQuoteSelector","exact":"RNNs only capture backward dependencies","prefix":"e next iteration (e.g. a model) ","suffix":" RNNs suffer from vanishing grad"}]}]}
>```
>%%
>*%%PREFIX%%e next iteration (e.g. a model)%%HIGHLIGHT%% ==RNNs only capture backward dependencies== %%POSTFIX%%RNNs suffer from vanishing grad*
>%%LINK%%[[#^llkr4va62n|show annotation]]
>%%COMMENT%%
>
>%%TAGS%%
>
^llkr4va62n


>%%
>```annotation-json
>{"created":"2024-10-01T14:50:50.308Z","updated":"2024-10-01T14:50:50.308Z","document":{"title":"03c Natural Language Generation Neural Network Methods","link":[{"href":"urn:x-pdf:d040e757a00f8c6dd8f715d9980d68cb"},{"href":"vault:/500 - attachments/computational_creativity_03c_natural_language_generation_neural_network_methods.pdf"}],"documentFingerprint":"d040e757a00f8c6dd8f715d9980d68cb"},"uri":"vault:/500 - attachments/computational_creativity_03c_natural_language_generation_neural_network_methods.pdf","target":[{"source":"vault:/500 - attachments/computational_creativity_03c_natural_language_generation_neural_network_methods.pdf","selector":[{"type":"TextPositionSelector","start":2034,"end":2147},{"type":"TextQuoteSelector","exact":"RNNs suffer from vanishing gradients Predictions based on most recent words Unable to produce long-range coherent","prefix":"y capture backward dependencies ","suffix":"Image credit: kdnuggets.comDisco"}]}]}
>```
>%%
>*%%PREFIX%%y capture backward dependencies%%HIGHLIGHT%% ==RNNs suffer from vanishing gradients Predictions based on most recent words Unable to produce long-range coherent== %%POSTFIX%%Image credit: kdnuggets.comDisco*
>%%LINK%%[[#^129yw2ufyx2|show annotation]]
>%%COMMENT%%
>
>%%TAGS%%
>
^129yw2ufyx2


>%%
>```annotation-json
>{"created":"2024-10-01T14:51:54.556Z","updated":"2024-10-01T14:51:54.556Z","document":{"title":"03c Natural Language Generation Neural Network Methods","link":[{"href":"urn:x-pdf:d040e757a00f8c6dd8f715d9980d68cb"},{"href":"vault:/500 - attachments/computational_creativity_03c_natural_language_generation_neural_network_methods.pdf"}],"documentFingerprint":"d040e757a00f8c6dd8f715d9980d68cb"},"uri":"vault:/500 - attachments/computational_creativity_03c_natural_language_generation_neural_network_methods.pdf","target":[{"source":"vault:/500 - attachments/computational_creativity_03c_natural_language_generation_neural_network_methods.pdf","selector":[{"type":"TextPositionSelector","start":2213,"end":2243},{"type":"TextQuoteSelector","exact":"The Vanishing Gradient Problem","prefix":"r the world at Leiden University","suffix":"As the RNN processes each input "}]}]}
>```
>%%
>*%%PREFIX%%r the world at Leiden University%%HIGHLIGHT%% ==The Vanishing Gradient Problem== %%POSTFIX%%As the RNN processes each input*
>%%LINK%%[[#^jo5wd0bokj|show annotation]]
>%%COMMENT%%
>
>%%TAGS%%
>
^jo5wd0bokj


>%%
>```annotation-json
>{"created":"2024-10-01T14:52:06.369Z","updated":"2024-10-01T14:52:06.369Z","document":{"title":"03c Natural Language Generation Neural Network Methods","link":[{"href":"urn:x-pdf:d040e757a00f8c6dd8f715d9980d68cb"},{"href":"vault:/500 - attachments/computational_creativity_03c_natural_language_generation_neural_network_methods.pdf"}],"documentFingerprint":"d040e757a00f8c6dd8f715d9980d68cb"},"uri":"vault:/500 - attachments/computational_creativity_03c_natural_language_generation_neural_network_methods.pdf","target":[{"source":"vault:/500 - attachments/computational_creativity_03c_natural_language_generation_neural_network_methods.pdf","selector":[{"type":"TextPositionSelector","start":2243,"end":2319},{"type":"TextQuoteSelector","exact":"As the RNN processes each input the influence of earlier words is diminished","prefix":"tyThe Vanishing Gradient Problem","suffix":" The operation of the RNN makes "}]}]}
>```
>%%
>*%%PREFIX%%tyThe Vanishing Gradient Problem%%HIGHLIGHT%% ==As the RNN processes each input the influence of earlier words is diminished== %%POSTFIX%%The operation of the RNN makes*
>%%LINK%%[[#^nsdn5sffc7|show annotation]]
>%%COMMENT%%
>
>%%TAGS%%
>
^nsdn5sffc7


>%%
>```annotation-json
>{"created":"2024-10-01T14:52:32.827Z","updated":"2024-10-01T14:52:32.827Z","document":{"title":"03c Natural Language Generation Neural Network Methods","link":[{"href":"urn:x-pdf:d040e757a00f8c6dd8f715d9980d68cb"},{"href":"vault:/500 - attachments/computational_creativity_03c_natural_language_generation_neural_network_methods.pdf"}],"documentFingerprint":"d040e757a00f8c6dd8f715d9980d68cb"},"uri":"vault:/500 - attachments/computational_creativity_03c_natural_language_generation_neural_network_methods.pdf","target":[{"source":"vault:/500 - attachments/computational_creativity_03c_natural_language_generation_neural_network_methods.pdf","selector":[{"type":"TextPositionSelector","start":2320,"end":2508},{"type":"TextQuoteSelector","exact":"The operation of the RNN makes the most recent inputs the most important in determining the output for the current input Output at   depends most on “room” and least on “walked” and “Jane”","prefix":" of earlier words is diminished ","suffix":"tJane walked into the room<latex"}]}]}
>```
>%%
>*%%PREFIX%%of earlier words is diminished%%HIGHLIGHT%% ==The operation of the RNN makes the most recent inputs the most important in determining the output for the current input Output at   depends most on “room” and least on “walked” and “Jane”== %%POSTFIX%%tJane walked into the room<latex*
>%%LINK%%[[#^6hya9mradqf|show annotation]]
>%%COMMENT%%
>
>%%TAGS%%
>
^6hya9mradqf


>%%
>```annotation-json
>{"created":"2024-10-01T14:52:45.263Z","text":"What is Long Short Term Memory (LSTM) and Gated Recurrent Unit (GRU) networks?","updated":"2024-10-01T14:52:45.263Z","document":{"title":"03c Natural Language Generation Neural Network Methods","link":[{"href":"urn:x-pdf:d040e757a00f8c6dd8f715d9980d68cb"},{"href":"vault:/500 - attachments/computational_creativity_03c_natural_language_generation_neural_network_methods.pdf"}],"documentFingerprint":"d040e757a00f8c6dd8f715d9980d68cb"},"uri":"vault:/500 - attachments/computational_creativity_03c_natural_language_generation_neural_network_methods.pdf","target":[{"source":"vault:/500 - attachments/computational_creativity_03c_natural_language_generation_neural_network_methods.pdf","selector":[{"type":"TextPositionSelector","start":5350,"end":5369},{"type":"TextQuoteSelector","exact":"LSTM and GRU Models","prefix":"r the world at Leiden University","suffix":"Long Short Term Memory (LSTM) an"}]}]}
>```
>%%
>*%%PREFIX%%r the world at Leiden University%%HIGHLIGHT%% ==LSTM and GRU Models== %%POSTFIX%%Long Short Term Memory (LSTM) an*
>%%LINK%%[[#^dxkkyyz78ds|show annotation]]
>%%COMMENT%%
>What is Long Short Term Memory (LSTM) and Gated Recurrent Unit (GRU) networks?
>%%TAGS%%
>#question
^dxkkyyz78ds


>%%
>```annotation-json
>{"created":"2024-10-01T15:01:08.963Z","updated":"2024-10-01T15:01:08.963Z","document":{"title":"03c Natural Language Generation Neural Network Methods","link":[{"href":"urn:x-pdf:d040e757a00f8c6dd8f715d9980d68cb"},{"href":"vault:/500 - attachments/computational_creativity_03c_natural_language_generation_neural_network_methods.pdf"}],"documentFingerprint":"d040e757a00f8c6dd8f715d9980d68cb"},"uri":"vault:/500 - attachments/computational_creativity_03c_natural_language_generation_neural_network_methods.pdf","target":[{"source":"vault:/500 - attachments/computational_creativity_03c_natural_language_generation_neural_network_methods.pdf","selector":[{"type":"TextPositionSelector","start":5369,"end":5484},{"type":"TextQuoteSelector","exact":"Long Short Term Memory (LSTM) and Gated Recurrent Unit (GRU) networks were designed to avoid the vanishing gradient","prefix":"en UniversityLSTM and GRU Models","suffix":" Consist of recurrent modules wi"}]}]}
>```
>%%
>*%%PREFIX%%en UniversityLSTM and GRU Models%%HIGHLIGHT%% ==Long Short Term Memory (LSTM) and Gated Recurrent Unit (GRU) networks were designed to avoid the vanishing gradient== %%POSTFIX%%Consist of recurrent modules wi*
>%%LINK%%[[#^fsfhgus5uer|show annotation]]
>%%COMMENT%%
>
>%%TAGS%%
>
^fsfhgus5uer


>%%
>```annotation-json
>{"created":"2024-10-01T15:03:32.149Z","updated":"2024-10-01T15:03:32.149Z","document":{"title":"03c Natural Language Generation Neural Network Methods","link":[{"href":"urn:x-pdf:d040e757a00f8c6dd8f715d9980d68cb"},{"href":"vault:/500 - attachments/computational_creativity_03c_natural_language_generation_neural_network_methods.pdf"}],"documentFingerprint":"d040e757a00f8c6dd8f715d9980d68cb"},"uri":"vault:/500 - attachments/computational_creativity_03c_natural_language_generation_neural_network_methods.pdf","target":[{"source":"vault:/500 - attachments/computational_creativity_03c_natural_language_generation_neural_network_methods.pdf","selector":[{"type":"TextPositionSelector","start":5605,"end":5667},{"type":"TextQuoteSelector","exact":"LSTM and GRU networks were the state-of-the-art until recently","prefix":"erations, i.e., internal state. ","suffix":" More effective at generating co"}]}]}
>```
>%%
>*%%PREFIX%%erations, i.e., internal state.%%HIGHLIGHT%% ==LSTM and GRU networks were the state-of-the-art until recently== %%POSTFIX%%More effective at generating co*
>%%LINK%%[[#^gluiqakcnov|show annotation]]
>%%COMMENT%%
>
>%%TAGS%%
>
^gluiqakcnov


>%%
>```annotation-json
>{"created":"2024-10-01T15:03:59.325Z","updated":"2024-10-01T15:03:59.325Z","document":{"title":"03c Natural Language Generation Neural Network Methods","link":[{"href":"urn:x-pdf:d040e757a00f8c6dd8f715d9980d68cb"},{"href":"vault:/500 - attachments/computational_creativity_03c_natural_language_generation_neural_network_methods.pdf"}],"documentFingerprint":"d040e757a00f8c6dd8f715d9980d68cb"},"uri":"vault:/500 - attachments/computational_creativity_03c_natural_language_generation_neural_network_methods.pdf","target":[{"source":"vault:/500 - attachments/computational_creativity_03c_natural_language_generation_neural_network_methods.pdf","selector":[{"type":"TextPositionSelector","start":5878,"end":5928},{"type":"TextQuoteSelector","exact":"LSTM and GRU tackle the vanishing gradient problem","prefix":" UniversityLSTM and GRU Networks","suffix":" LSTM and GRU networks consist o"}]}]}
>```
>%%
>*%%PREFIX%%UniversityLSTM and GRU Networks%%HIGHLIGHT%% ==LSTM and GRU tackle the vanishing gradient problem== %%POSTFIX%%LSTM and GRU networks consist o*
>%%LINK%%[[#^hka3nhumtu|show annotation]]
>%%COMMENT%%
>
>%%TAGS%%
>
^hka3nhumtu


>%%
>```annotation-json
>{"created":"2024-10-01T15:05:17.543Z","updated":"2024-10-01T15:05:17.543Z","document":{"title":"03c Natural Language Generation Neural Network Methods","link":[{"href":"urn:x-pdf:d040e757a00f8c6dd8f715d9980d68cb"},{"href":"vault:/500 - attachments/computational_creativity_03c_natural_language_generation_neural_network_methods.pdf"}],"documentFingerprint":"d040e757a00f8c6dd8f715d9980d68cb"},"uri":"vault:/500 - attachments/computational_creativity_03c_natural_language_generation_neural_network_methods.pdf","target":[{"source":"vault:/500 - attachments/computational_creativity_03c_natural_language_generation_neural_network_methods.pdf","selector":[{"type":"TextPositionSelector","start":5929,"end":6026},{"type":"TextQuoteSelector","exact":"LSTM and GRU networks consist of units with gates that regulate the flow of information over time","prefix":" the vanishing gradient problem ","suffix":" Gates allow network to learn th"}]}]}
>```
>%%
>*%%PREFIX%%the vanishing gradient problem%%HIGHLIGHT%% ==LSTM and GRU networks consist of units with gates that regulate the flow of information over time== %%POSTFIX%%Gates allow network to learn th*
>%%LINK%%[[#^e5uw6flbbj|show annotation]]
>%%COMMENT%%
>
>%%TAGS%%
>
^e5uw6flbbj


>%%
>```annotation-json
>{"created":"2024-10-01T15:06:41.189Z","updated":"2024-10-01T15:06:41.189Z","document":{"title":"03c Natural Language Generation Neural Network Methods","link":[{"href":"urn:x-pdf:d040e757a00f8c6dd8f715d9980d68cb"},{"href":"vault:/500 - attachments/computational_creativity_03c_natural_language_generation_neural_network_methods.pdf"}],"documentFingerprint":"d040e757a00f8c6dd8f715d9980d68cb"},"uri":"vault:/500 - attachments/computational_creativity_03c_natural_language_generation_neural_network_methods.pdf","target":[{"source":"vault:/500 - attachments/computational_creativity_03c_natural_language_generation_neural_network_methods.pdf","selector":[{"type":"TextPositionSelector","start":6278,"end":6303},{"type":"TextQuoteSelector","exact":"Sigmoid Function as Gates","prefix":"r the world at Leiden University","suffix":"Sigmoid Function squashes inputs"}]}]}
>```
>%%
>*%%PREFIX%%r the world at Leiden University%%HIGHLIGHT%% ==Sigmoid Function as Gates== %%POSTFIX%%Sigmoid Function squashes inputs*
>%%LINK%%[[#^u006ro3azc|show annotation]]
>%%COMMENT%%
>
>%%TAGS%%
>
^u006ro3azc


>%%
>```annotation-json
>{"created":"2024-10-01T15:06:45.458Z","text":"Why use the Sigmoid function as a gate? ","updated":"2024-10-01T15:06:45.458Z","document":{"title":"03c Natural Language Generation Neural Network Methods","link":[{"href":"urn:x-pdf:d040e757a00f8c6dd8f715d9980d68cb"},{"href":"vault:/500 - attachments/computational_creativity_03c_natural_language_generation_neural_network_methods.pdf"}],"documentFingerprint":"d040e757a00f8c6dd8f715d9980d68cb"},"uri":"vault:/500 - attachments/computational_creativity_03c_natural_language_generation_neural_network_methods.pdf","target":[{"source":"vault:/500 - attachments/computational_creativity_03c_natural_language_generation_neural_network_methods.pdf","selector":[{"type":"TextPositionSelector","start":6303,"end":6530},{"type":"TextQuoteSelector","exact":"Sigmoid Function squashes inputs into range 0..1 Useful for constructing gates because: Multiplying anything by 0 results in 0, i.e., deletes (or forgets) it Multiplying anything by 1 results in the same value, i.e., retains it","prefix":"versitySigmoid Function as Gates","suffix":"Discover the world at Leiden Uni"}]}]}
>```
>%%
>*%%PREFIX%%versitySigmoid Function as Gates%%HIGHLIGHT%% ==Sigmoid Function squashes inputs into range 0..1 Useful for constructing gates because: Multiplying anything by 0 results in 0, i.e., deletes (or forgets) it Multiplying anything by 1 results in the same value, i.e., retains it== %%POSTFIX%%Discover the world at Leiden Uni*
>%%LINK%%[[#^78veydlom3t|show annotation]]
>%%COMMENT%%
>Why use the Sigmoid function as a gate? 
>%%TAGS%%
>#question
^78veydlom3t


>%%
>```annotation-json
>{"created":"2024-10-01T15:08:14.264Z","updated":"2024-10-01T15:08:14.264Z","document":{"title":"03c Natural Language Generation Neural Network Methods","link":[{"href":"urn:x-pdf:d040e757a00f8c6dd8f715d9980d68cb"},{"href":"vault:/500 - attachments/computational_creativity_03c_natural_language_generation_neural_network_methods.pdf"}],"documentFingerprint":"d040e757a00f8c6dd8f715d9980d68cb"},"uri":"vault:/500 - attachments/computational_creativity_03c_natural_language_generation_neural_network_methods.pdf","target":[{"source":"vault:/500 - attachments/computational_creativity_03c_natural_language_generation_neural_network_methods.pdf","selector":[{"type":"TextPositionSelector","start":6027,"end":6096},{"type":"TextQuoteSelector","exact":"Gates allow network to learn the most important information to retain","prefix":"e flow of information over time ","suffix":"Schematic of an LSTM unitForget "}]}]}
>```
>%%
>*%%PREFIX%%e flow of information over time%%HIGHLIGHT%% ==Gates allow network to learn the most important information to retain== %%POSTFIX%%Schematic of an LSTM unitForget*
>%%LINK%%[[#^99bz7hm3jia|show annotation]]
>%%COMMENT%%
>
>%%TAGS%%
>
^99bz7hm3jia


>%%
>```annotation-json
>{"created":"2024-10-01T15:09:40.088Z","text":"How does the Gated Recurrent Unit work?","updated":"2024-10-01T15:09:40.088Z","document":{"title":"03c Natural Language Generation Neural Network Methods","link":[{"href":"urn:x-pdf:d040e757a00f8c6dd8f715d9980d68cb"},{"href":"vault:/500 - attachments/computational_creativity_03c_natural_language_generation_neural_network_methods.pdf"}],"documentFingerprint":"d040e757a00f8c6dd8f715d9980d68cb"},"uri":"vault:/500 - attachments/computational_creativity_03c_natural_language_generation_neural_network_methods.pdf","target":[{"source":"vault:/500 - attachments/computational_creativity_03c_natural_language_generation_neural_network_methods.pdf","selector":[{"type":"TextPositionSelector","start":6713,"end":6961},{"type":"TextQuoteSelector","exact":"GRU works like LSTM Cell state is contained within hidden state Reset gate works like forget gate in LSTM Update gate combines the operation of input and output gates in LSTM GRU requires fewer tensor operations, so can be slightly quicker to train","prefix":" UniversityLSTM and GRU Networks","suffix":"Schematic of a GRUReset GateUpda"}]}]}
>```
>%%
>*%%PREFIX%%UniversityLSTM and GRU Networks%%HIGHLIGHT%% ==GRU works like LSTM Cell state is contained within hidden state Reset gate works like forget gate in LSTM Update gate combines the operation of input and output gates in LSTM GRU requires fewer tensor operations, so can be slightly quicker to train== %%POSTFIX%%Schematic of a GRUReset GateUpda*
>%%LINK%%[[#^ql9a705e3k|show annotation]]
>%%COMMENT%%
>How does the Gated Recurrent Unit work?
>%%TAGS%%
>#question
^ql9a705e3k


>%%
>```annotation-json
>{"created":"2024-10-01T15:16:14.472Z","text":"What are the advantages and disadvantages of RNNs and Gated Units?","updated":"2024-10-01T15:16:14.472Z","document":{"title":"03c Natural Language Generation Neural Network Methods","link":[{"href":"urn:x-pdf:d040e757a00f8c6dd8f715d9980d68cb"},{"href":"vault:/500 - attachments/computational_creativity_03c_natural_language_generation_neural_network_methods.pdf"}],"documentFingerprint":"d040e757a00f8c6dd8f715d9980d68cb"},"uri":"vault:/500 - attachments/computational_creativity_03c_natural_language_generation_neural_network_methods.pdf","target":[{"source":"vault:/500 - attachments/computational_creativity_03c_natural_language_generation_neural_network_methods.pdf","selector":[{"type":"TextPositionSelector","start":7039,"end":7091},{"type":"TextQuoteSelector","exact":"Advantages and Disadvantages of RNNs and Gated Units","prefix":"r the world at Leiden University","suffix":"Advantages and disadvantages of "}]}]}
>```
>%%
>*%%PREFIX%%r the world at Leiden University%%HIGHLIGHT%% ==Advantages and Disadvantages of RNNs and Gated Units== %%POSTFIX%%Advantages and disadvantages of*
>%%LINK%%[[#^hu806rwonyh|show annotation]]
>%%COMMENT%%
>What are the advantages and disadvantages of RNNs and Gated Units?
>%%TAGS%%
>#question
^hu806rwonyh


>%%
>```annotation-json
>{"created":"2024-10-01T15:17:30.330Z","updated":"2024-10-01T15:17:30.330Z","document":{"title":"03c Natural Language Generation Neural Network Methods","link":[{"href":"urn:x-pdf:d040e757a00f8c6dd8f715d9980d68cb"},{"href":"vault:/500 - attachments/computational_creativity_03c_natural_language_generation_neural_network_methods.pdf"}],"documentFingerprint":"d040e757a00f8c6dd8f715d9980d68cb"},"uri":"vault:/500 - attachments/computational_creativity_03c_natural_language_generation_neural_network_methods.pdf","target":[{"source":"vault:/500 - attachments/computational_creativity_03c_natural_language_generation_neural_network_methods.pdf","selector":[{"type":"TextPositionSelector","start":7091,"end":7417},{"type":"TextQuoteSelector","exact":"Advantages and disadvantages of using recurrent neural networks (RNNs) + RNNs provide a more space efficient modelling approach than e.g. Markov models – RNNs suffer from the problem of “vanishing gradients” over relatively short sequences – Standard RNNs are unidirectional and only take into account history of tokens so far","prefix":"vantages of RNNs and Gated Units","suffix":" Advantages and disadvantages of"}]}]}
>```
>%%
>*%%PREFIX%%vantages of RNNs and Gated Units%%HIGHLIGHT%% ==Advantages and disadvantages of using recurrent neural networks (RNNs) + RNNs provide a more space efficient modelling approach than e.g. Markov models – RNNs suffer from the problem of “vanishing gradients” over relatively short sequences – Standard RNNs are unidirectional and only take into account history of tokens so far== %%POSTFIX%%Advantages and disadvantages of*
>%%LINK%%[[#^1g37uuk7fun|show annotation]]
>%%COMMENT%%
>
>%%TAGS%%
>
^1g37uuk7fun


>%%
>```annotation-json
>{"created":"2024-10-01T15:17:45.717Z","updated":"2024-10-01T15:17:45.717Z","document":{"title":"03c Natural Language Generation Neural Network Methods","link":[{"href":"urn:x-pdf:d040e757a00f8c6dd8f715d9980d68cb"},{"href":"vault:/500 - attachments/computational_creativity_03c_natural_language_generation_neural_network_methods.pdf"}],"documentFingerprint":"d040e757a00f8c6dd8f715d9980d68cb"},"uri":"vault:/500 - attachments/computational_creativity_03c_natural_language_generation_neural_network_methods.pdf","target":[{"source":"vault:/500 - attachments/computational_creativity_03c_natural_language_generation_neural_network_methods.pdf","selector":[{"type":"TextPositionSelector","start":7418,"end":7813},{"type":"TextQuoteSelector","exact":"Advantages and disadvantages of using gated units (LSTMs and GRUs) + Explicitly attempt to overcome problem of vanishing gradients by learning to control the flow of information through time – Still suffer from “vanishing gradients” but over longer sequence lengths – Standard LSTMs and GRUs are still unidirectional – Cannot be easily parallelised because next output depends on previous output","prefix":"ccount history of tokens so far ","suffix":"Discover the world at Leiden Uni"}]}]}
>```
>%%
>*%%PREFIX%%ccount history of tokens so far%%HIGHLIGHT%% ==Advantages and disadvantages of using gated units (LSTMs and GRUs) + Explicitly attempt to overcome problem of vanishing gradients by learning to control the flow of information through time – Still suffer from “vanishing gradients” but over longer sequence lengths – Standard LSTMs and GRUs are still unidirectional – Cannot be easily parallelised because next output depends on previous output== %%POSTFIX%%Discover the world at Leiden Uni*
>%%LINK%%[[#^pcfb1d8cal|show annotation]]
>%%COMMENT%%
>
>%%TAGS%%
>
^pcfb1d8cal


>%%
>```annotation-json
>{"created":"2024-10-01T15:18:43.934Z","text":"Problems with RNNs, GRUs and LSTMs?","updated":"2024-10-01T15:18:43.934Z","document":{"title":"03c Natural Language Generation Neural Network Methods","link":[{"href":"urn:x-pdf:d040e757a00f8c6dd8f715d9980d68cb"},{"href":"vault:/500 - attachments/computational_creativity_03c_natural_language_generation_neural_network_methods.pdf"}],"documentFingerprint":"d040e757a00f8c6dd8f715d9980d68cb"},"uri":"vault:/500 - attachments/computational_creativity_03c_natural_language_generation_neural_network_methods.pdf","target":[{"source":"vault:/500 - attachments/computational_creativity_03c_natural_language_generation_neural_network_methods.pdf","selector":[{"type":"TextPositionSelector","start":7954,"end":8161},{"type":"TextQuoteSelector","exact":"Problems with RNNs, GRUs and LSTMs: All process words sequentially, in the order they appear: Poor retention of context (even in GRUs and LSTMs) Hard to parallelise: each input relies on the previous output ","prefix":"at Leiden UniversityTransformers","suffix":"Transformers (e.g. BERT, GPT, Ll"}]}]}
>```
>%%
>*%%PREFIX%%at Leiden UniversityTransformers%%HIGHLIGHT%% ==Problems with RNNs, GRUs and LSTMs: All process words sequentially, in the order they appear: Poor retention of context (even in GRUs and LSTMs) Hard to parallelise: each input relies on the previous output== %%POSTFIX%%Transformers (e.g. BERT, GPT, Ll*
>%%LINK%%[[#^93hfv24rsy|show annotation]]
>%%COMMENT%%
>Problems with RNNs, GRUs and LSTMs?
>%%TAGS%%
>#question
^93hfv24rsy


>%%
>```annotation-json
>{"created":"2024-10-01T15:19:24.519Z","text":"How do transformers work?","updated":"2024-10-01T15:19:24.519Z","document":{"title":"03c Natural Language Generation Neural Network Methods","link":[{"href":"urn:x-pdf:d040e757a00f8c6dd8f715d9980d68cb"},{"href":"vault:/500 - attachments/computational_creativity_03c_natural_language_generation_neural_network_methods.pdf"}],"documentFingerprint":"d040e757a00f8c6dd8f715d9980d68cb"},"uri":"vault:/500 - attachments/computational_creativity_03c_natural_language_generation_neural_network_methods.pdf","target":[{"source":"vault:/500 - attachments/computational_creativity_03c_natural_language_generation_neural_network_methods.pdf","selector":[{"type":"TextPositionSelector","start":8161,"end":8509},{"type":"TextQuoteSelector","exact":"Transformers (e.g. BERT, GPT, Llama, etc.): Transformers use an attention mechanism: “Attends” to words most useful in predicting next word Process an input sequence of words all at once Map dependencies between words regardless of distance Highly parallelisable = train larger models at a faster rate Use contextual clues to solve ambiguity issues","prefix":"t relies on the previous output ","suffix":"Discover the world at Leiden Uni"}]}]}
>```
>%%
>*%%PREFIX%%t relies on the previous output%%HIGHLIGHT%% ==Transformers (e.g. BERT, GPT, Llama, etc.): Transformers use an attention mechanism: “Attends” to words most useful in predicting next word Process an input sequence of words all at once Map dependencies between words regardless of distance Highly parallelisable = train larger models at a faster rate Use contextual clues to solve ambiguity issues== %%POSTFIX%%Discover the world at Leiden Uni*
>%%LINK%%[[#^jre73yowlk|show annotation]]
>%%COMMENT%%
>How do transformers work?
>%%TAGS%%
>#question
^jre73yowlk


>%%
>```annotation-json
>{"created":"2024-10-01T15:23:27.709Z","text":"What is bidirectional encoder representation from transformers (BERT)?","updated":"2024-10-01T15:23:27.709Z","document":{"title":"03c Natural Language Generation Neural Network Methods","link":[{"href":"urn:x-pdf:d040e757a00f8c6dd8f715d9980d68cb"},{"href":"vault:/500 - attachments/computational_creativity_03c_natural_language_generation_neural_network_methods.pdf"}],"documentFingerprint":"d040e757a00f8c6dd8f715d9980d68cb"},"uri":"vault:/500 - attachments/computational_creativity_03c_natural_language_generation_neural_network_methods.pdf","target":[{"source":"vault:/500 - attachments/computational_creativity_03c_natural_language_generation_neural_network_methods.pdf","selector":[{"type":"TextPositionSelector","start":8548,"end":8610},{"type":"TextQuoteSelector","exact":"Bidirectional Encoder Representations from Transformers (BERT)","prefix":"r the world at Leiden University","suffix":"BERT and GPT are large pre-train"}]}]}
>```
>%%
>*%%PREFIX%%r the world at Leiden University%%HIGHLIGHT%% ==Bidirectional Encoder Representations from Transformers (BERT)== %%POSTFIX%%BERT and GPT are large pre-train*
>%%LINK%%[[#^gtg8cotwovi|show annotation]]
>%%COMMENT%%
>What is bidirectional encoder representation from transformers (BERT)?
>%%TAGS%%
>#question
^gtg8cotwovi


>%%
>```annotation-json
>{"created":"2024-10-01T15:24:12.468Z","updated":"2024-10-01T15:24:12.468Z","document":{"title":"03c Natural Language Generation Neural Network Methods","link":[{"href":"urn:x-pdf:d040e757a00f8c6dd8f715d9980d68cb"},{"href":"vault:/500 - attachments/computational_creativity_03c_natural_language_generation_neural_network_methods.pdf"}],"documentFingerprint":"d040e757a00f8c6dd8f715d9980d68cb"},"uri":"vault:/500 - attachments/computational_creativity_03c_natural_language_generation_neural_network_methods.pdf","target":[{"source":"vault:/500 - attachments/computational_creativity_03c_natural_language_generation_neural_network_methods.pdf","selector":[{"type":"TextPositionSelector","start":8610,"end":8717},{"type":"TextQuoteSelector","exact":"BERT and GPT are large pre-trained language models Trained an very large datasets to produce general models","prefix":"tations from Transformers (BERT)","suffix":" Bidirectional Encoder Represent"}]}]}
>```
>%%
>*%%PREFIX%%tations from Transformers (BERT)%%HIGHLIGHT%% ==BERT and GPT are large pre-trained language models Trained an very large datasets to produce general models== %%POSTFIX%%Bidirectional Encoder Represent*
>%%LINK%%[[#^oqsee8cfaoo|show annotation]]
>%%COMMENT%%
>
>%%TAGS%%
>
^oqsee8cfaoo


>%%
>```annotation-json
>{"created":"2024-10-01T15:24:50.226Z","updated":"2024-10-01T15:24:50.226Z","document":{"title":"03c Natural Language Generation Neural Network Methods","link":[{"href":"urn:x-pdf:d040e757a00f8c6dd8f715d9980d68cb"},{"href":"vault:/500 - attachments/computational_creativity_03c_natural_language_generation_neural_network_methods.pdf"}],"documentFingerprint":"d040e757a00f8c6dd8f715d9980d68cb"},"uri":"vault:/500 - attachments/computational_creativity_03c_natural_language_generation_neural_network_methods.pdf","target":[{"source":"vault:/500 - attachments/computational_creativity_03c_natural_language_generation_neural_network_methods.pdf","selector":[{"type":"TextPositionSelector","start":8718,"end":8858},{"type":"TextQuoteSelector","exact":"Bidirectional Encoder Representations from Transformers (BERT) Bidirectionally trained 2.5 billion words and contains 345 million parameters","prefix":"asets to produce general models ","suffix":" Optimised for predicting masked"}]}]}
>```
>%%
>*%%PREFIX%%asets to produce general models%%HIGHLIGHT%% ==Bidirectional Encoder Representations from Transformers (BERT) Bidirectionally trained 2.5 billion words and contains 345 million parameters== %%POSTFIX%%Optimised for predicting masked*
>%%LINK%%[[#^v7ieeliisxr|show annotation]]
>%%COMMENT%%
>
>%%TAGS%%
>
^v7ieeliisxr


>%%
>```annotation-json
>{"created":"2024-10-01T15:24:53.871Z","updated":"2024-10-01T15:24:53.871Z","document":{"title":"03c Natural Language Generation Neural Network Methods","link":[{"href":"urn:x-pdf:d040e757a00f8c6dd8f715d9980d68cb"},{"href":"vault:/500 - attachments/computational_creativity_03c_natural_language_generation_neural_network_methods.pdf"}],"documentFingerprint":"d040e757a00f8c6dd8f715d9980d68cb"},"uri":"vault:/500 - attachments/computational_creativity_03c_natural_language_generation_neural_network_methods.pdf","target":[{"source":"vault:/500 - attachments/computational_creativity_03c_natural_language_generation_neural_network_methods.pdf","selector":[{"type":"TextPositionSelector","start":8859,"end":8909},{"type":"TextQuoteSelector","exact":"Optimised for predicting masked words (Masked LM) ","prefix":"contains 345 million parameters ","suffix":"Mary had a little lamb its ____ "}]}]}
>```
>%%
>*%%PREFIX%%contains 345 million parameters%%HIGHLIGHT%% ==Optimised for predicting masked words (Masked LM)== %%POSTFIX%%Mary had a little lamb its ____*
>%%LINK%%[[#^57k0brvrhbn|show annotation]]
>%%COMMENT%%
>
>%%TAGS%%
>
^57k0brvrhbn


>%%
>```annotation-json
>{"created":"2024-10-01T15:24:57.316Z","updated":"2024-10-01T15:24:57.316Z","document":{"title":"03c Natural Language Generation Neural Network Methods","link":[{"href":"urn:x-pdf:d040e757a00f8c6dd8f715d9980d68cb"},{"href":"vault:/500 - attachments/computational_creativity_03c_natural_language_generation_neural_network_methods.pdf"}],"documentFingerprint":"d040e757a00f8c6dd8f715d9980d68cb"},"uri":"vault:/500 - attachments/computational_creativity_03c_natural_language_generation_neural_network_methods.pdf","target":[{"source":"vault:/500 - attachments/computational_creativity_03c_natural_language_generation_neural_network_methods.pdf","selector":[{"type":"TextPositionSelector","start":8959,"end":9004},{"type":"TextQuoteSelector","exact":"Combined with Next Sentence Prediction (NSP) ","prefix":"lamb its ____ as white as snow. ","suffix":"i.e. how sentences related to ea"}]}]}
>```
>%%
>*%%PREFIX%%lamb its ____ as white as snow.%%HIGHLIGHT%% ==Combined with Next Sentence Prediction (NSP)== %%POSTFIX%%i.e. how sentences related to ea*
>%%LINK%%[[#^yxjs1gmah6f|show annotation]]
>%%COMMENT%%
>
>%%TAGS%%
>
^yxjs1gmah6f


>%%
>```annotation-json
>{"created":"2024-10-01T15:25:01.779Z","updated":"2024-10-01T15:25:01.779Z","document":{"title":"03c Natural Language Generation Neural Network Methods","link":[{"href":"urn:x-pdf:d040e757a00f8c6dd8f715d9980d68cb"},{"href":"vault:/500 - attachments/computational_creativity_03c_natural_language_generation_neural_network_methods.pdf"}],"documentFingerprint":"d040e757a00f8c6dd8f715d9980d68cb"},"uri":"vault:/500 - attachments/computational_creativity_03c_natural_language_generation_neural_network_methods.pdf","target":[{"source":"vault:/500 - attachments/computational_creativity_03c_natural_language_generation_neural_network_methods.pdf","selector":[{"type":"TextPositionSelector","start":9045,"end":9097},{"type":"TextQuoteSelector","exact":"Models both left-to-right and right-to-left contexts","prefix":"sentences related to each other ","suffix":" Raise your oars when you get to"}]}]}
>```
>%%
>*%%PREFIX%%sentences related to each other%%HIGHLIGHT%% ==Models both left-to-right and right-to-left contexts== %%POSTFIX%%Raise your oars when you get to*
>%%LINK%%[[#^iocx3g281s|show annotation]]
>%%COMMENT%%
>
>%%TAGS%%
>
^iocx3g281s


>%%
>```annotation-json
>{"created":"2024-10-01T15:25:14.731Z","text":"What is a generative pre-trained transformer (GPT)?","updated":"2024-10-01T15:25:14.731Z","document":{"title":"03c Natural Language Generation Neural Network Methods","link":[{"href":"urn:x-pdf:d040e757a00f8c6dd8f715d9980d68cb"},{"href":"vault:/500 - attachments/computational_creativity_03c_natural_language_generation_neural_network_methods.pdf"}],"documentFingerprint":"d040e757a00f8c6dd8f715d9980d68cb"},"uri":"vault:/500 - attachments/computational_creativity_03c_natural_language_generation_neural_network_methods.pdf","target":[{"source":"vault:/500 - attachments/computational_creativity_03c_natural_language_generation_neural_network_methods.pdf","selector":[{"type":"TextPositionSelector","start":9301,"end":9341},{"type":"TextQuoteSelector","exact":"Generative Pre-trained Transformer (GPT)","prefix":"r the world at Leiden University","suffix":"Generative Pre-trained Transform"}]}]}
>```
>%%
>*%%PREFIX%%r the world at Leiden University%%HIGHLIGHT%% ==Generative Pre-trained Transformer (GPT)== %%POSTFIX%%Generative Pre-trained Transform*
>%%LINK%%[[#^6ir3mc96pd|show annotation]]
>%%COMMENT%%
>What is a generative pre-trained transformer (GPT)?
>%%TAGS%%
>#question
^6ir3mc96pd


>%%
>```annotation-json
>{"created":"2024-10-01T15:25:58.858Z","updated":"2024-10-01T15:25:58.858Z","document":{"title":"03c Natural Language Generation Neural Network Methods","link":[{"href":"urn:x-pdf:d040e757a00f8c6dd8f715d9980d68cb"},{"href":"vault:/500 - attachments/computational_creativity_03c_natural_language_generation_neural_network_methods.pdf"}],"documentFingerprint":"d040e757a00f8c6dd8f715d9980d68cb"},"uri":"vault:/500 - attachments/computational_creativity_03c_natural_language_generation_neural_network_methods.pdf","target":[{"source":"vault:/500 - attachments/computational_creativity_03c_natural_language_generation_neural_network_methods.pdf","selector":[{"type":"TextPositionSelector","start":9341,"end":9473},{"type":"TextQuoteSelector","exact":"Generative Pre-trained Transformer (e.g. GPT-2, GPT-3, GPT-4 etc.) GPT models are unidirectional Trained on much more data than BERT","prefix":"ve Pre-trained Transformer (GPT)","suffix":" e.g. GPT-3 was trained on 45 Te"}]}]}
>```
>%%
>*%%PREFIX%%ve Pre-trained Transformer (GPT)%%HIGHLIGHT%% ==Generative Pre-trained Transformer (e.g. GPT-2, GPT-3, GPT-4 etc.) GPT models are unidirectional Trained on much more data than BERT== %%POSTFIX%%e.g. GPT-3 was trained on 45 Te*
>%%LINK%%[[#^lw4m07cfec|show annotation]]
>%%COMMENT%%
>
>%%TAGS%%
>
^lw4m07cfec


>%%
>```annotation-json
>{"created":"2024-10-01T15:26:05.948Z","updated":"2024-10-01T15:26:05.948Z","document":{"title":"03c Natural Language Generation Neural Network Methods","link":[{"href":"urn:x-pdf:d040e757a00f8c6dd8f715d9980d68cb"},{"href":"vault:/500 - attachments/computational_creativity_03c_natural_language_generation_neural_network_methods.pdf"}],"documentFingerprint":"d040e757a00f8c6dd8f715d9980d68cb"},"uri":"vault:/500 - attachments/computational_creativity_03c_natural_language_generation_neural_network_methods.pdf","target":[{"source":"vault:/500 - attachments/computational_creativity_03c_natural_language_generation_neural_network_methods.pdf","selector":[{"type":"TextPositionSelector","start":9521,"end":9555},{"type":"TextQuoteSelector","exact":"Networks are much larger than BERT","prefix":"trained on 45 Terabytes of data ","suffix":" GPT-2 has 2 billion parameters "}]}]}
>```
>%%
>*%%PREFIX%%trained on 45 Terabytes of data%%HIGHLIGHT%% ==Networks are much larger than BERT== %%POSTFIX%%GPT-2 has 2 billion parameters*
>%%LINK%%[[#^m3bchht1c3i|show annotation]]
>%%COMMENT%%
>
>%%TAGS%%
>
^m3bchht1c3i


>%%
>```annotation-json
>{"created":"2024-10-01T15:26:13.184Z","updated":"2024-10-01T15:26:13.184Z","document":{"title":"03c Natural Language Generation Neural Network Methods","link":[{"href":"urn:x-pdf:d040e757a00f8c6dd8f715d9980d68cb"},{"href":"vault:/500 - attachments/computational_creativity_03c_natural_language_generation_neural_network_methods.pdf"}],"documentFingerprint":"d040e757a00f8c6dd8f715d9980d68cb"},"uri":"vault:/500 - attachments/computational_creativity_03c_natural_language_generation_neural_network_methods.pdf","target":[{"source":"vault:/500 - attachments/computational_creativity_03c_natural_language_generation_neural_network_methods.pdf","selector":[{"type":"TextPositionSelector","start":9654,"end":9715},{"type":"TextQuoteSelector","exact":"GPT models typically require less data than BERT to fine-tune","prefix":"T-4 has 1.7 trillion parameters ","suffix":" See: Guardian Article written b"}]}]}
>```
>%%
>*%%PREFIX%%T-4 has 1.7 trillion parameters%%HIGHLIGHT%% ==GPT models typically require less data than BERT to fine-tune== %%POSTFIX%%See: Guardian Article written b*
>%%LINK%%[[#^m572pggfors|show annotation]]
>%%COMMENT%%
>
>%%TAGS%%
>
^m572pggfors


>%%
>```annotation-json
>{"created":"2024-10-01T15:27:27.759Z","updated":"2024-10-01T15:27:27.759Z","document":{"title":"03c Natural Language Generation Neural Network Methods","link":[{"href":"urn:x-pdf:d040e757a00f8c6dd8f715d9980d68cb"},{"href":"vault:/500 - attachments/computational_creativity_03c_natural_language_generation_neural_network_methods.pdf"}],"documentFingerprint":"d040e757a00f8c6dd8f715d9980d68cb"},"uri":"vault:/500 - attachments/computational_creativity_03c_natural_language_generation_neural_network_methods.pdf","target":[{"source":"vault:/500 - attachments/computational_creativity_03c_natural_language_generation_neural_network_methods.pdf","selector":[{"type":"TextPositionSelector","start":9805,"end":9900},{"type":"TextQuoteSelector","exact":"Transformers have become one of the most widely adopted machine learning models in recent years","prefix":"at Leiden UniversityTransformers","suffix":" The model was introduced in the"}]}]}
>```
>%%
>*%%PREFIX%%at Leiden UniversityTransformers%%HIGHLIGHT%% ==Transformers have become one of the most widely adopted machine learning models in recent years== %%POSTFIX%%The model was introduced in the*
>%%LINK%%[[#^sa60hh4frhr|show annotation]]
>%%COMMENT%%
>
>%%TAGS%%
>
^sa60hh4frhr


>%%
>```annotation-json
>{"created":"2024-10-01T15:27:34.035Z","text":"What are transformers?","updated":"2024-10-01T15:27:34.035Z","document":{"title":"03c Natural Language Generation Neural Network Methods","link":[{"href":"urn:x-pdf:d040e757a00f8c6dd8f715d9980d68cb"},{"href":"vault:/500 - attachments/computational_creativity_03c_natural_language_generation_neural_network_methods.pdf"}],"documentFingerprint":"d040e757a00f8c6dd8f715d9980d68cb"},"uri":"vault:/500 - attachments/computational_creativity_03c_natural_language_generation_neural_network_methods.pdf","target":[{"source":"vault:/500 - attachments/computational_creativity_03c_natural_language_generation_neural_network_methods.pdf","selector":[{"type":"TextPositionSelector","start":9793,"end":9805},{"type":"TextQuoteSelector","exact":"Transformers","prefix":"r the world at Leiden University","suffix":"Transformers have become one of "}]}]}
>```
>%%
>*%%PREFIX%%r the world at Leiden University%%HIGHLIGHT%% ==Transformers== %%POSTFIX%%Transformers have become one of*
>%%LINK%%[[#^jyaijows2n9|show annotation]]
>%%COMMENT%%
>What are transformers?
>%%TAGS%%
>#question
^jyaijows2n9


>%%
>```annotation-json
>{"created":"2024-10-01T15:28:00.309Z","updated":"2024-10-01T15:28:00.309Z","document":{"title":"03c Natural Language Generation Neural Network Methods","link":[{"href":"urn:x-pdf:d040e757a00f8c6dd8f715d9980d68cb"},{"href":"vault:/500 - attachments/computational_creativity_03c_natural_language_generation_neural_network_methods.pdf"}],"documentFingerprint":"d040e757a00f8c6dd8f715d9980d68cb"},"uri":"vault:/500 - attachments/computational_creativity_03c_natural_language_generation_neural_network_methods.pdf","target":[{"source":"vault:/500 - attachments/computational_creativity_03c_natural_language_generation_neural_network_methods.pdf","selector":[{"type":"TextPositionSelector","start":9991,"end":10112},{"type":"TextQuoteSelector","exact":"The model has been successfully applied to text (e.g. GPT), audio (e.g. Music Transformer) and visual (Dall-E) generation","prefix":" Need by Vaswani et al. in 2017 ","suffix":"Source: The Illustrated Transfom"}]}]}
>```
>%%
>*%%PREFIX%%Need by Vaswani et al. in 2017%%HIGHLIGHT%% ==The model has been successfully applied to text (e.g. GPT), audio (e.g. Music Transformer) and visual (Dall-E) generation== %%POSTFIX%%Source: The Illustrated Transfom*
>%%LINK%%[[#^65ye2ptv3sp|show annotation]]
>%%COMMENT%%
>
>%%TAGS%%
>
^65ye2ptv3sp


>%%
>```annotation-json
>{"created":"2024-10-01T15:32:22.979Z","updated":"2024-10-01T15:32:22.979Z","document":{"title":"03c Natural Language Generation Neural Network Methods","link":[{"href":"urn:x-pdf:d040e757a00f8c6dd8f715d9980d68cb"},{"href":"vault:/500 - attachments/computational_creativity_03c_natural_language_generation_neural_network_methods.pdf"}],"documentFingerprint":"d040e757a00f8c6dd8f715d9980d68cb"},"uri":"vault:/500 - attachments/computational_creativity_03c_natural_language_generation_neural_network_methods.pdf","target":[{"source":"vault:/500 - attachments/computational_creativity_03c_natural_language_generation_neural_network_methods.pdf","selector":[{"type":"TextPositionSelector","start":10200,"end":10273},{"type":"TextQuoteSelector","exact":"Transformers were initially introduced as a form of encoder-decoder model","prefix":"Leiden UniversityEncoder-Decoder","suffix":": This type of model is used for"}]}]}
>```
>%%
>*%%PREFIX%%Leiden UniversityEncoder-Decoder%%HIGHLIGHT%% ==Transformers were initially introduced as a form of encoder-decoder model== %%POSTFIX%%: This type of model is used for*
>%%LINK%%[[#^dsfchzd1kwh|show annotation]]
>%%COMMENT%%
>
>%%TAGS%%
>
^dsfchzd1kwh


>%%
>```annotation-json
>{"created":"2024-10-01T15:32:40.005Z","updated":"2024-10-01T15:32:40.005Z","document":{"title":"03c Natural Language Generation Neural Network Methods","link":[{"href":"urn:x-pdf:d040e757a00f8c6dd8f715d9980d68cb"},{"href":"vault:/500 - attachments/computational_creativity_03c_natural_language_generation_neural_network_methods.pdf"}],"documentFingerprint":"d040e757a00f8c6dd8f715d9980d68cb"},"uri":"vault:/500 - attachments/computational_creativity_03c_natural_language_generation_neural_network_methods.pdf","target":[{"source":"vault:/500 - attachments/computational_creativity_03c_natural_language_generation_neural_network_methods.pdf","selector":[{"type":"TextPositionSelector","start":10275,"end":10492},{"type":"TextQuoteSelector","exact":"This type of model is used for sequence-to-sequence applications, e.g., translation from one language to another We will follow this description to get a full description of the model before looking at text generation","prefix":" form of encoder-decoder model: ","suffix":"Source: The Illustrated Transfom"}]}]}
>```
>%%
>*%%PREFIX%%form of encoder-decoder model:%%HIGHLIGHT%% ==This type of model is used for sequence-to-sequence applications, e.g., translation from one language to another We will follow this description to get a full description of the model before looking at text generation== %%POSTFIX%%Source: The Illustrated Transfom*
>%%LINK%%[[#^0gp3hsmnkl2v|show annotation]]
>%%COMMENT%%
>
>%%TAGS%%
>
^0gp3hsmnkl2v


>%%
>```annotation-json
>{"created":"2024-10-01T15:33:26.281Z","updated":"2024-10-01T15:33:26.281Z","document":{"title":"03c Natural Language Generation Neural Network Methods","link":[{"href":"urn:x-pdf:d040e757a00f8c6dd8f715d9980d68cb"},{"href":"vault:/500 - attachments/computational_creativity_03c_natural_language_generation_neural_network_methods.pdf"}],"documentFingerprint":"d040e757a00f8c6dd8f715d9980d68cb"},"uri":"vault:/500 - attachments/computational_creativity_03c_natural_language_generation_neural_network_methods.pdf","target":[{"source":"vault:/500 - attachments/computational_creativity_03c_natural_language_generation_neural_network_methods.pdf","selector":[{"type":"TextPositionSelector","start":10580,"end":10654},{"type":"TextQuoteSelector","exact":"Tranformer-based models typically contain a stack of encoders and decoders","prefix":"Leiden UniversityEncoder-Decoder","suffix":": One of the strengths of transf"}]}]}
>```
>%%
>*%%PREFIX%%Leiden UniversityEncoder-Decoder%%HIGHLIGHT%% ==Tranformer-based models typically contain a stack of encoders and decoders== %%POSTFIX%%: One of the strengths of transf*
>%%LINK%%[[#^6c6bc05tb1s|show annotation]]
>%%COMMENT%%
>
>%%TAGS%%
>
^6c6bc05tb1s


>%%
>```annotation-json
>{"created":"2024-10-01T15:33:36.931Z","updated":"2024-10-01T15:33:36.931Z","document":{"title":"03c Natural Language Generation Neural Network Methods","link":[{"href":"urn:x-pdf:d040e757a00f8c6dd8f715d9980d68cb"},{"href":"vault:/500 - attachments/computational_creativity_03c_natural_language_generation_neural_network_methods.pdf"}],"documentFingerprint":"d040e757a00f8c6dd8f715d9980d68cb"},"uri":"vault:/500 - attachments/computational_creativity_03c_natural_language_generation_neural_network_methods.pdf","target":[{"source":"vault:/500 - attachments/computational_creativity_03c_natural_language_generation_neural_network_methods.pdf","selector":[{"type":"TextPositionSelector","start":10656,"end":10817},{"type":"TextQuoteSelector","exact":"One of the strengths of transformers is that they work well when stacked The encoders build an internal representation, which is used as an input to the decoders","prefix":"stack of encoders and decoders: ","suffix":"Source: The Illustrated Transfom"}]}]}
>```
>%%
>*%%PREFIX%%stack of encoders and decoders:%%HIGHLIGHT%% ==One of the strengths of transformers is that they work well when stacked The encoders build an internal representation, which is used as an input to the decoders== %%POSTFIX%%Source: The Illustrated Transfom*
>%%LINK%%[[#^ytve4ghj54|show annotation]]
>%%COMMENT%%
>
>%%TAGS%%
>
^ytve4ghj54


>%%
>```annotation-json
>{"created":"2024-10-01T15:34:12.040Z","updated":"2024-10-01T15:34:12.040Z","document":{"title":"03c Natural Language Generation Neural Network Methods","link":[{"href":"urn:x-pdf:d040e757a00f8c6dd8f715d9980d68cb"},{"href":"vault:/500 - attachments/computational_creativity_03c_natural_language_generation_neural_network_methods.pdf"}],"documentFingerprint":"d040e757a00f8c6dd8f715d9980d68cb"},"uri":"vault:/500 - attachments/computational_creativity_03c_natural_language_generation_neural_network_methods.pdf","target":[{"source":"vault:/500 - attachments/computational_creativity_03c_natural_language_generation_neural_network_methods.pdf","selector":[{"type":"TextPositionSelector","start":10905,"end":10921},{"type":"TextQuoteSelector","exact":"Encoders combine","prefix":"Leiden UniversityEncoder-Decoder","suffix":": Self-attention layer Focuses o"}]}]}
>```
>%%
>*%%PREFIX%%Leiden UniversityEncoder-Decoder%%HIGHLIGHT%% ==Encoders combine== %%POSTFIX%%: Self-attention layer Focuses o*
>%%LINK%%[[#^3qi4qijxtum|show annotation]]
>%%COMMENT%%
>
>%%TAGS%%
>
^3qi4qijxtum


>%%
>```annotation-json
>{"created":"2024-10-01T15:34:15.661Z","updated":"2024-10-01T15:34:15.661Z","document":{"title":"03c Natural Language Generation Neural Network Methods","link":[{"href":"urn:x-pdf:d040e757a00f8c6dd8f715d9980d68cb"},{"href":"vault:/500 - attachments/computational_creativity_03c_natural_language_generation_neural_network_methods.pdf"}],"documentFingerprint":"d040e757a00f8c6dd8f715d9980d68cb"},"uri":"vault:/500 - attachments/computational_creativity_03c_natural_language_generation_neural_network_methods.pdf","target":[{"source":"vault:/500 - attachments/computational_creativity_03c_natural_language_generation_neural_network_methods.pdf","selector":[{"type":"TextPositionSelector","start":10923,"end":11012},{"type":"TextQuoteSelector","exact":"Self-attention layer Focuses on words in the input sequence as it encodes a specific word","prefix":"ncoder-DecoderEncoders combine: ","suffix":" Feed-forward network Transforms"}]}]}
>```
>%%
>*%%PREFIX%%ncoder-DecoderEncoders combine:%%HIGHLIGHT%% ==Self-attention layer Focuses on words in the input sequence as it encodes a specific word== %%POSTFIX%%Feed-forward network Transforms*
>%%LINK%%[[#^s8fx0bcqul|show annotation]]
>%%COMMENT%%
>
>%%TAGS%%
>
^s8fx0bcqul


>%%
>```annotation-json
>{"created":"2024-10-01T15:34:48.578Z","updated":"2024-10-01T15:34:48.578Z","document":{"title":"03c Natural Language Generation Neural Network Methods","link":[{"href":"urn:x-pdf:d040e757a00f8c6dd8f715d9980d68cb"},{"href":"vault:/500 - attachments/computational_creativity_03c_natural_language_generation_neural_network_methods.pdf"}],"documentFingerprint":"d040e757a00f8c6dd8f715d9980d68cb"},"uri":"vault:/500 - attachments/computational_creativity_03c_natural_language_generation_neural_network_methods.pdf","target":[{"source":"vault:/500 - attachments/computational_creativity_03c_natural_language_generation_neural_network_methods.pdf","selector":[{"type":"TextPositionSelector","start":11013,"end":11111},{"type":"TextQuoteSelector","exact":"Feed-forward network Transforms output of the self-attention layer into an internal representation","prefix":"e as it encodes a specific word ","suffix":"Source: The Illustrated Transfom"}]}]}
>```
>%%
>*%%PREFIX%%e as it encodes a specific word%%HIGHLIGHT%% ==Feed-forward network Transforms output of the self-attention layer into an internal representation== %%POSTFIX%%Source: The Illustrated Transfom*
>%%LINK%%[[#^oy9k87n2b6a|show annotation]]
>%%COMMENT%%
>
>%%TAGS%%
>
^oy9k87n2b6a


>%%
>```annotation-json
>{"created":"2024-10-01T15:35:33.643Z","updated":"2024-10-01T15:35:33.643Z","document":{"title":"03c Natural Language Generation Neural Network Methods","link":[{"href":"urn:x-pdf:d040e757a00f8c6dd8f715d9980d68cb"},{"href":"vault:/500 - attachments/computational_creativity_03c_natural_language_generation_neural_network_methods.pdf"}],"documentFingerprint":"d040e757a00f8c6dd8f715d9980d68cb"},"uri":"vault:/500 - attachments/computational_creativity_03c_natural_language_generation_neural_network_methods.pdf","target":[{"source":"vault:/500 - attachments/computational_creativity_03c_natural_language_generation_neural_network_methods.pdf","selector":[{"type":"TextPositionSelector","start":11199,"end":11270},{"type":"TextQuoteSelector","exact":"Decoders combine the self-attention layer and feed-forward network with","prefix":"Leiden UniversityEncoder-Decoder","suffix":": Encoder-decoder attention Assi"}]}]}
>```
>%%
>*%%PREFIX%%Leiden UniversityEncoder-Decoder%%HIGHLIGHT%% ==Decoders combine the self-attention layer and feed-forward network with== %%POSTFIX%%: Encoder-decoder attention Assi*
>%%LINK%%[[#^42337r78sh5|show annotation]]
>%%COMMENT%%
>
>%%TAGS%%
>
^42337r78sh5


>%%
>```annotation-json
>{"created":"2024-10-01T15:35:44.400Z","updated":"2024-10-01T15:35:44.400Z","document":{"title":"03c Natural Language Generation Neural Network Methods","link":[{"href":"urn:x-pdf:d040e757a00f8c6dd8f715d9980d68cb"},{"href":"vault:/500 - attachments/computational_creativity_03c_natural_language_generation_neural_network_methods.pdf"}],"documentFingerprint":"d040e757a00f8c6dd8f715d9980d68cb"},"uri":"vault:/500 - attachments/computational_creativity_03c_natural_language_generation_neural_network_methods.pdf","target":[{"source":"vault:/500 - attachments/computational_creativity_03c_natural_language_generation_neural_network_methods.pdf","selector":[{"type":"TextPositionSelector","start":11272,"end":11366},{"type":"TextQuoteSelector","exact":"Encoder-decoder attention Assists the decoder to focus on relevant parts of the input sentence","prefix":" and feed-forward network with: ","suffix":"Source: The Illustrated Transfom"}]}]}
>```
>%%
>*%%PREFIX%%and feed-forward network with:%%HIGHLIGHT%% ==Encoder-decoder attention Assists the decoder to focus on relevant parts of the input sentence== %%POSTFIX%%Source: The Illustrated Transfom*
>%%LINK%%[[#^nxcrfgy1r2|show annotation]]
>%%COMMENT%%
>
>%%TAGS%%
>
^nxcrfgy1r2


>%%
>```annotation-json
>{"created":"2024-10-01T15:35:56.747Z","updated":"2024-10-01T15:35:56.747Z","document":{"title":"03c Natural Language Generation Neural Network Methods","link":[{"href":"urn:x-pdf:d040e757a00f8c6dd8f715d9980d68cb"},{"href":"vault:/500 - attachments/computational_creativity_03c_natural_language_generation_neural_network_methods.pdf"}],"documentFingerprint":"d040e757a00f8c6dd8f715d9980d68cb"},"uri":"vault:/500 - attachments/computational_creativity_03c_natural_language_generation_neural_network_methods.pdf","target":[{"source":"vault:/500 - attachments/computational_creativity_03c_natural_language_generation_neural_network_methods.pdf","selector":[{"type":"TextPositionSelector","start":11453,"end":11534},{"type":"TextQuoteSelector","exact":"Self-attention allows transformer blocks to associate together words in the input","prefix":" Leiden UniversitySelf-Attention","suffix":" In the example shown here, self"}]}]}
>```
>%%
>*%%PREFIX%%Leiden UniversitySelf-Attention%%HIGHLIGHT%% ==Self-attention allows transformer blocks to associate together words in the input== %%POSTFIX%%In the example shown here, self*
>%%LINK%%[[#^77sko801jzy|show annotation]]
>%%COMMENT%%
>
>%%TAGS%%
>
^77sko801jzy


>%%
>```annotation-json
>{"created":"2024-10-01T15:37:34.821Z","updated":"2024-10-01T15:37:34.821Z","document":{"title":"03c Natural Language Generation Neural Network Methods","link":[{"href":"urn:x-pdf:d040e757a00f8c6dd8f715d9980d68cb"},{"href":"vault:/500 - attachments/computational_creativity_03c_natural_language_generation_neural_network_methods.pdf"}],"documentFingerprint":"d040e757a00f8c6dd8f715d9980d68cb"},"uri":"vault:/500 - attachments/computational_creativity_03c_natural_language_generation_neural_network_methods.pdf","target":[{"source":"vault:/500 - attachments/computational_creativity_03c_natural_language_generation_neural_network_methods.pdf","selector":[{"type":"TextPositionSelector","start":11647,"end":11750},{"type":"TextQuoteSelector","exact":"All of the words being associated are represented by the list of vectors presented to the first encoder","prefix":"n the input including “animal”. ","suffix":" Source: The Illustrated Transfo"}]}]}
>```
>%%
>*%%PREFIX%%n the input including “animal”.%%HIGHLIGHT%% ==All of the words being associated are represented by the list of vectors presented to the first encoder== %%POSTFIX%%Source: The Illustrated Transfo*
>%%LINK%%[[#^5irc73bb8al|show annotation]]
>%%COMMENT%%
>
>%%TAGS%%
>
^5irc73bb8al


>%%
>```annotation-json
>{"created":"2024-10-01T15:37:54.593Z","updated":"2024-10-01T15:37:54.593Z","document":{"title":"03c Natural Language Generation Neural Network Methods","link":[{"href":"urn:x-pdf:d040e757a00f8c6dd8f715d9980d68cb"},{"href":"vault:/500 - attachments/computational_creativity_03c_natural_language_generation_neural_network_methods.pdf"}],"documentFingerprint":"d040e757a00f8c6dd8f715d9980d68cb"},"uri":"vault:/500 - attachments/computational_creativity_03c_natural_language_generation_neural_network_methods.pdf","target":[{"source":"vault:/500 - attachments/computational_creativity_03c_natural_language_generation_neural_network_methods.pdf","selector":[{"type":"TextPositionSelector","start":11846,"end":11901},{"type":"TextQuoteSelector","exact":"The result of multi-headed attention can be visualised ","prefix":"UniversityMulti-headed Attention","suffix":" Shows how it permits different "}]}]}
>```
>%%
>*%%PREFIX%%UniversityMulti-headed Attention%%HIGHLIGHT%% ==The result of multi-headed attention can be visualised== %%POSTFIX%%Shows how it permits different*
>%%LINK%%[[#^jo6vfrvqhaa|show annotation]]
>%%COMMENT%%
>
>%%TAGS%%
>
^jo6vfrvqhaa


>%%
>```annotation-json
>{"created":"2024-10-01T15:39:36.049Z","updated":"2024-10-01T15:39:36.049Z","document":{"title":"03c Natural Language Generation Neural Network Methods","link":[{"href":"urn:x-pdf:d040e757a00f8c6dd8f715d9980d68cb"},{"href":"vault:/500 - attachments/computational_creativity_03c_natural_language_generation_neural_network_methods.pdf"}],"documentFingerprint":"d040e757a00f8c6dd8f715d9980d68cb"},"uri":"vault:/500 - attachments/computational_creativity_03c_natural_language_generation_neural_network_methods.pdf","target":[{"source":"vault:/500 - attachments/computational_creativity_03c_natural_language_generation_neural_network_methods.pdf","selector":[{"type":"TextPositionSelector","start":12100,"end":12155},{"type":"TextQuoteSelector","exact":"The result of multi-headed attention can be visualised ","prefix":"UniversityMulti-headed Attention","suffix":" Shows how it permits different "}]}]}
>```
>%%
>*%%PREFIX%%UniversityMulti-headed Attention%%HIGHLIGHT%% ==The result of multi-headed attention can be visualised== %%POSTFIX%%Shows how it permits different*
>%%LINK%%[[#^vjgnjxepo2b|show annotation]]
>%%COMMENT%%
>
>%%TAGS%%
>
^vjgnjxepo2b


>%%
>```annotation-json
>{"created":"2024-10-01T15:41:13.979Z","updated":"2024-10-01T15:41:13.979Z","document":{"title":"03c Natural Language Generation Neural Network Methods","link":[{"href":"urn:x-pdf:d040e757a00f8c6dd8f715d9980d68cb"},{"href":"vault:/500 - attachments/computational_creativity_03c_natural_language_generation_neural_network_methods.pdf"}],"documentFingerprint":"d040e757a00f8c6dd8f715d9980d68cb"},"uri":"vault:/500 - attachments/computational_creativity_03c_natural_language_generation_neural_network_methods.pdf","target":[{"source":"vault:/500 - attachments/computational_creativity_03c_natural_language_generation_neural_network_methods.pdf","selector":[{"type":"TextPositionSelector","start":12464,"end":12544},{"type":"TextQuoteSelector","exact":"In addition to word embedding, each input word has its position encoded as well ","prefix":"en UniversityPositional Encoding","suffix":"The input for each word is a the"}]}]}
>```
>%%
>*%%PREFIX%%en UniversityPositional Encoding%%HIGHLIGHT%% ==In addition to word embedding, each input word has its position encoded as well== %%POSTFIX%%The input for each word is a the*
>%%LINK%%[[#^cro1vx4tip|show annotation]]
>%%COMMENT%%
>
>%%TAGS%%
>
^cro1vx4tip


>%%
>```annotation-json
>{"created":"2024-10-01T15:41:50.897Z","updated":"2024-10-01T15:41:50.897Z","document":{"title":"03c Natural Language Generation Neural Network Methods","link":[{"href":"urn:x-pdf:d040e757a00f8c6dd8f715d9980d68cb"},{"href":"vault:/500 - attachments/computational_creativity_03c_natural_language_generation_neural_network_methods.pdf"}],"documentFingerprint":"d040e757a00f8c6dd8f715d9980d68cb"},"uri":"vault:/500 - attachments/computational_creativity_03c_natural_language_generation_neural_network_methods.pdf","target":[{"source":"vault:/500 - attachments/computational_creativity_03c_natural_language_generation_neural_network_methods.pdf","selector":[{"type":"TextPositionSelector","start":12544,"end":12620},{"type":"TextQuoteSelector","exact":"The input for each word is a the embedding added to the positional encoding.","prefix":"as its position encoded as well ","suffix":" Positional vectors follow a pat"}]}]}
>```
>%%
>*%%PREFIX%%as its position encoded as well%%HIGHLIGHT%% ==The input for each word is a the embedding added to the positional encoding.== %%POSTFIX%%Positional vectors follow a pat*
>%%LINK%%[[#^fhpxzgm4i38|show annotation]]
>%%COMMENT%%
>
>%%TAGS%%
>
^fhpxzgm4i38


>%%
>```annotation-json
>{"created":"2024-10-01T15:41:59.621Z","updated":"2024-10-01T15:41:59.621Z","document":{"title":"03c Natural Language Generation Neural Network Methods","link":[{"href":"urn:x-pdf:d040e757a00f8c6dd8f715d9980d68cb"},{"href":"vault:/500 - attachments/computational_creativity_03c_natural_language_generation_neural_network_methods.pdf"}],"documentFingerprint":"d040e757a00f8c6dd8f715d9980d68cb"},"uri":"vault:/500 - attachments/computational_creativity_03c_natural_language_generation_neural_network_methods.pdf","target":[{"source":"vault:/500 - attachments/computational_creativity_03c_natural_language_generation_neural_network_methods.pdf","selector":[{"type":"TextPositionSelector","start":12621,"end":12745},{"type":"TextQuoteSelector","exact":"Positional vectors follow a pattern that the model learns to determine the position of each word, or distance between words.","prefix":"ded to the positional encoding. ","suffix":"Source: The Illustrated Transfom"}]}]}
>```
>%%
>*%%PREFIX%%ded to the positional encoding.%%HIGHLIGHT%% ==Positional vectors follow a pattern that the model learns to determine the position of each word, or distance between words.== %%POSTFIX%%Source: The Illustrated Transfom*
>%%LINK%%[[#^85o3w5mgciv|show annotation]]
>%%COMMENT%%
>
>%%TAGS%%
>
^85o3w5mgciv


>%%
>```annotation-json
>{"created":"2024-10-01T15:42:19.592Z","updated":"2024-10-01T15:42:19.592Z","document":{"title":"03c Natural Language Generation Neural Network Methods","link":[{"href":"urn:x-pdf:d040e757a00f8c6dd8f715d9980d68cb"},{"href":"vault:/500 - attachments/computational_creativity_03c_natural_language_generation_neural_network_methods.pdf"}],"documentFingerprint":"d040e757a00f8c6dd8f715d9980d68cb"},"uri":"vault:/500 - attachments/computational_creativity_03c_natural_language_generation_neural_network_methods.pdf","target":[{"source":"vault:/500 - attachments/computational_creativity_03c_natural_language_generation_neural_network_methods.pdf","selector":[{"type":"TextPositionSelector","start":12837,"end":13004},{"type":"TextQuoteSelector","exact":"To accommodate potentially very long input sequences in a fixed length encoding the positional data is encoded in a pattern that grows slowly across the encoded vector","prefix":"en UniversityPositional Encoding","suffix":" In this example, the pattern co"}]}]}
>```
>%%
>*%%PREFIX%%en UniversityPositional Encoding%%HIGHLIGHT%% ==To accommodate potentially very long input sequences in a fixed length encoding the positional data is encoded in a pattern that grows slowly across the encoded vector== %%POSTFIX%%In this example, the pattern co*
>%%LINK%%[[#^5ld0zxizlb|show annotation]]
>%%COMMENT%%
>
>%%TAGS%%
>
^5ld0zxizlb


>%%
>```annotation-json
>{"created":"2024-10-01T15:42:51.825Z","updated":"2024-10-01T15:42:51.825Z","document":{"title":"03c Natural Language Generation Neural Network Methods","link":[{"href":"urn:x-pdf:d040e757a00f8c6dd8f715d9980d68cb"},{"href":"vault:/500 - attachments/computational_creativity_03c_natural_language_generation_neural_network_methods.pdf"}],"documentFingerprint":"d040e757a00f8c6dd8f715d9980d68cb"},"uri":"vault:/500 - attachments/computational_creativity_03c_natural_language_generation_neural_network_methods.pdf","target":[{"source":"vault:/500 - attachments/computational_creativity_03c_natural_language_generation_neural_network_methods.pdf","selector":[{"type":"TextPositionSelector","start":13210,"end":13377},{"type":"TextQuoteSelector","exact":"To accommodate potentially very long input sequences in a fixed length encoding the positional data is encoded in a pattern that grows slowly across the encoded vector","prefix":"en UniversityPositional Encoding","suffix":" In this example, the pattern co"}]}]}
>```
>%%
>*%%PREFIX%%en UniversityPositional Encoding%%HIGHLIGHT%% ==To accommodate potentially very long input sequences in a fixed length encoding the positional data is encoded in a pattern that grows slowly across the encoded vector== %%POSTFIX%%In this example, the pattern co*
>%%LINK%%[[#^6qohp09aeok|show annotation]]
>%%COMMENT%%
>
>%%TAGS%%
>
^6qohp09aeok


>%%
>```annotation-json
>{"created":"2024-10-01T15:44:43.812Z","updated":"2024-10-01T15:44:43.812Z","document":{"title":"03c Natural Language Generation Neural Network Methods","link":[{"href":"urn:x-pdf:d040e757a00f8c6dd8f715d9980d68cb"},{"href":"vault:/500 - attachments/computational_creativity_03c_natural_language_generation_neural_network_methods.pdf"}],"documentFingerprint":"d040e757a00f8c6dd8f715d9980d68cb"},"uri":"vault:/500 - attachments/computational_creativity_03c_natural_language_generation_neural_network_methods.pdf","target":[{"source":"vault:/500 - attachments/computational_creativity_03c_natural_language_generation_neural_network_methods.pdf","selector":[{"type":"TextPositionSelector","start":13695,"end":13737},{"type":"TextQuoteSelector","exact":"The decoder is very similar to the encoder","prefix":"orld at Leiden UniversityDecoder","suffix":" An additional encoder-decoder a"}]}]}
>```
>%%
>*%%PREFIX%%orld at Leiden UniversityDecoder%%HIGHLIGHT%% ==The decoder is very similar to the encoder== %%POSTFIX%%An additional encoder-decoder a*
>%%LINK%%[[#^osfkacq4s4o|show annotation]]
>%%COMMENT%%
>
>%%TAGS%%
>
^osfkacq4s4o


>%%
>```annotation-json
>{"created":"2024-10-01T15:44:50.413Z","updated":"2024-10-01T15:44:50.413Z","document":{"title":"03c Natural Language Generation Neural Network Methods","link":[{"href":"urn:x-pdf:d040e757a00f8c6dd8f715d9980d68cb"},{"href":"vault:/500 - attachments/computational_creativity_03c_natural_language_generation_neural_network_methods.pdf"}],"documentFingerprint":"d040e757a00f8c6dd8f715d9980d68cb"},"uri":"vault:/500 - attachments/computational_creativity_03c_natural_language_generation_neural_network_methods.pdf","target":[{"source":"vault:/500 - attachments/computational_creativity_03c_natural_language_generation_neural_network_methods.pdf","selector":[{"type":"TextPositionSelector","start":13738,"end":13865},{"type":"TextQuoteSelector","exact":"An additional encoder-decoder attention layer, supporting the use of internal representation to attend to features of the input","prefix":" is very similar to the encoder ","suffix":" The first decoder block may hav"}]}]}
>```
>%%
>*%%PREFIX%%is very similar to the encoder%%HIGHLIGHT%% ==An additional encoder-decoder attention layer, supporting the use of internal representation to attend to features of the input== %%POSTFIX%%The first decoder block may hav*
>%%LINK%%[[#^dgldkiqnix|show annotation]]
>%%COMMENT%%
>
>%%TAGS%%
>
^dgldkiqnix


>%%
>```annotation-json
>{"created":"2024-10-01T15:45:01.670Z","updated":"2024-10-01T15:45:01.670Z","document":{"title":"03c Natural Language Generation Neural Network Methods","link":[{"href":"urn:x-pdf:d040e757a00f8c6dd8f715d9980d68cb"},{"href":"vault:/500 - attachments/computational_creativity_03c_natural_language_generation_neural_network_methods.pdf"}],"documentFingerprint":"d040e757a00f8c6dd8f715d9980d68cb"},"uri":"vault:/500 - attachments/computational_creativity_03c_natural_language_generation_neural_network_methods.pdf","target":[{"source":"vault:/500 - attachments/computational_creativity_03c_natural_language_generation_neural_network_methods.pdf","selector":[{"type":"TextPositionSelector","start":13866,"end":13986},{"type":"TextQuoteSelector","exact":"The first decoder block may have an additional mask to force it to attend only to the previous tokens to the current one","prefix":"attend to features of the input ","suffix":"Source: The Illustrated Transfom"}]}]}
>```
>%%
>*%%PREFIX%%attend to features of the input%%HIGHLIGHT%% ==The first decoder block may have an additional mask to force it to attend only to the previous tokens to the current one== %%POSTFIX%%Source: The Illustrated Transfom*
>%%LINK%%[[#^njoa63n46mk|show annotation]]
>%%COMMENT%%
>
>%%TAGS%%
>
^njoa63n46mk


>%%
>```annotation-json
>{"created":"2024-10-01T15:46:01.114Z","updated":"2024-10-01T15:46:01.114Z","document":{"title":"03c Natural Language Generation Neural Network Methods","link":[{"href":"urn:x-pdf:d040e757a00f8c6dd8f715d9980d68cb"},{"href":"vault:/500 - attachments/computational_creativity_03c_natural_language_generation_neural_network_methods.pdf"}],"documentFingerprint":"d040e757a00f8c6dd8f715d9980d68cb"},"uri":"vault:/500 - attachments/computational_creativity_03c_natural_language_generation_neural_network_methods.pdf","target":[{"source":"vault:/500 - attachments/computational_creativity_03c_natural_language_generation_neural_network_methods.pdf","selector":[{"type":"TextPositionSelector","start":14753,"end":15277},{"type":"TextQuoteSelector","exact":"Learning good models of language is hard RNNs suffer from “vanishing gradient” GRU and LSTM attempt to address “vanishing gradient” but are still hard to parallelise Transformers represent the state-of-the-art Pre-trained transformers are designed to be fine-tuned with a small number of examples because computing power required makes training from scratch impractical Active research areas include finding ways to make the training of transformer networks more efficient both in terms of network size and dataset required ","prefix":"ConclusionNeural Network Models ","suffix":" More Information Less Informati"}]}]}
>```
>%%
>*%%PREFIX%%ConclusionNeural Network Models%%HIGHLIGHT%% ==Learning good models of language is hard RNNs suffer from “vanishing gradient” GRU and LSTM attempt to address “vanishing gradient” but are still hard to parallelise Transformers represent the state-of-the-art Pre-trained transformers are designed to be fine-tuned with a small number of examples because computing power required makes training from scratch impractical Active research areas include finding ways to make the training of transformer networks more efficient both in terms of network size and dataset required== %%POSTFIX%%More Information Less Informati*
>%%LINK%%[[#^ctt1fl625p5|show annotation]]
>%%COMMENT%%
>
>%%TAGS%%
>
^ctt1fl625p5
