"use client";

import { useState, FormEvent, ChangeEvent } from "react"; // Se não usar ícones, pode remover
import axios from "axios"

export default function Home() {
  // Estados para controlar os inputs do formulário
  const [files, setFiles] = useState<File[]>([]);
  const [selectedOption, setSelectedOption] = useState<string>("");
  const [selectedDate, setSelectedDate] = useState<string>("");
  const [loading, setLoading] = useState<boolean>(false);

  // Manipulador para o input de múltiplos arquivos
  const handleFileChange = (e: ChangeEvent<HTMLInputElement>) => {
    if (e.target.files) {
      setFiles(Array.from(e.target.files));
    }
  };

  // Função de envio (onde você chamará a sua API FastAPI)
  const handleSubmit = async (e: FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    setLoading(true);

    const formData = new FormData();

    files.forEach((file) => {
      formData.append("files", file);
    });

    formData.append("option", selectedOption);
    formData.append("date", selectedDate);

    try {

      const response = await axios.post("http://localhost:8000/orders/", formData);
      const data = response.data;

      console.log("Sucesso:", data);

      alert(`${data.length} pedido(s) enviado(s) com sucesso.`);
    } catch (error) {
      console.error("Erro ao enviar:", error);
      alert("Erro ao enviar os dados.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <main className="min-h-screen bg-zinc-950 text-zinc-100 flex items-center justify-center p-4">
      <div className="w-full max-w-lg bg-zinc-900 border border-zinc-800 rounded-2xl p-8 shadow-2xl">
        <h1 className="text-2xl font-bold mb-2 text-white">Painel de Envio</h1>
        <p className="text-zinc-400 text-sm mb-6">
          Preencha os dados, selecione os arquivos e escolha a data desejada.
        </p>

        <form onSubmit={handleSubmit} className="space-y-5">
          
          {/* Input de Múltiplos Arquivos */}
          <div>
            <label className="block text-sm font-medium text-zinc-300 mb-2">
              Arquivos (Múltiplos)
            </label>
            <input
              type="file"
              multiple
              required
              onChange={handleFileChange}
              className="w-full text-sm text-zinc-400 file:mr-4 file:py-2 file:px-4 file:rounded-xl file:border-0 file:text-sm file:font-semibold file:bg-zinc-800 file:text-zinc-200 hover:file:bg-zinc-700 cursor-pointer border border-zinc-800 rounded-xl bg-zinc-950 p-2"
            />
            {files.length > 0 && (
              <ul className="mt-2 text-xs text-zinc-400 space-y-1">
                {files.map((file, index) => (
                  <li key={index} className="truncate">
                    📎 {file.name} ({Math.round(file.size / 1024)} KB)
                  </li>
                ))}
              </ul>
            )}
          </div>

          {/* Select de Opções */}
          <div>
            <label className="block text-sm font-medium text-zinc-300 mb-2">
              Categoria / Opção
            </label>
            <select
              value={selectedOption}
              onChange={(e) => setSelectedOption(e.target.value)}
              required
              className="w-full bg-zinc-950 border border-zinc-800 rounded-xl px-4 py-2.5 text-zinc-200 focus:outline-none focus:border-zinc-500 transition-colors"
            >
              <option value="" disabled>
                Selecione uma opção...
              </option>
              <option value="opcao_1">Auditoria e Relatórios</option>
              <option value="opcao_2">Contestação de Comissões</option>
              <option value="opcao_3">Processamento Interno</option>
            </select>
          </div>

          {/* Input de Data (Calendário) */}
          <div>
            <label className="block text-sm font-medium text-zinc-300 mb-2">
              Data de Referência
            </label>
            <input
              type="date"
              value={selectedDate}
              onChange={(e) => setSelectedDate(e.target.value)}
              required
              className="w-full bg-zinc-950 border border-zinc-800 rounded-xl px-4 py-2.5 text-zinc-200 focus:outline-none focus:border-zinc-500 transition-colors color-scheme-dark"
            />
          </div>

          {/* Botão de Envio */}
          <button
            type="submit"
            disabled={loading}
            className="w-full bg-indigo-600 hover:bg-indigo-500 text-white font-medium py-3 rounded-xl transition-all shadow-lg hover:shadow-indigo-500/20 disabled:opacity-50 cursor-pointer mt-4"
          >
            {loading ? "Enviando..." : "Enviar Dados"}
          </button>
        </form>
      </div>
    </main>
  );
}